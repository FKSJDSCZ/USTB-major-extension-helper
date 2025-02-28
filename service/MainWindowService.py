import json
import re
import logging

from lxml import etree
from PySide6.QtCore import QTimer, QObject, Signal
from PySide6.QtNetwork import QNetworkReply
from PySide6.QtGui import QStandardItem

from model.MainWindowModel import MainWindowModel
from entity.NetworkAccessManager import NetworkAccessManager
from entity.GuiLogger import guiLogger

rootDomain = "https://mec.ustb.edu.cn"


class MainWindowService(QObject):
	courseListUpdated = Signal()

	def __init__(self, manager: NetworkAccessManager, mainWindowModel: MainWindowModel):
		super().__init__()
		self.model_: MainWindowModel = mainWindowModel
		self.manager_: NetworkAccessManager = manager
		self.timer_: QTimer = QTimer()

		self.queryCourseListUrl_: str = str()
		self.chooseCourseUrl_: str = str()
		self.dropCourseUrl_: str = str()

		self.timer_.timeout.connect(self._onTimerTimeout)

	def getOptions(self, htmlString: str) -> None:
		homepageHtml: etree._Element = etree.HTML(htmlString)
		scripts = homepageHtml.xpath("//script/text()")
		for script in scripts:
			if script:
				# matches[2] has patten like "/stu/stuQk?termid=...&pcid=...&xkfs=1&xsfl=1&sxxsfl="
				matches = re.findall(r"url\s*:\s*['\"](.*?)['\"]", script)
				self.queryCourseListUrl_ = rootDomain + matches[0]
				self.chooseCourseUrl_ = rootDomain + matches[2] + "1"
				self.dropCourseUrl_ = rootDomain + matches[3]
				break

		for element in homepageHtml.xpath("//div[contains(@class, 'tag kcfw')]"):
			self.model_.majorRangeList_.append(element.text)

		for element in homepageHtml.xpath("//div[contains(@class, 'tag syxs')]"):
			self.model_.studentTypeList_.append(element.text)

		for element in homepageHtml.xpath("//select[@id='kkxq']/option"):
			self.model_.campusList_.append(element.text if element.text else "不限")

		for element in homepageHtml.xpath("//select[@id='yxsh']/option"):
			self.model_.collegeList_.append(element.text if element.text else "不限")
			self.model_.collegeValueList_.append(element.xpath("./@value")[0])

		for element in homepageHtml.xpath("//select[@id='skqszc']/option"):
			self.model_.startWeekList_.append(element.text if element.text else "不限")
			self.model_.startWeekValueList_.append(element.xpath("./@value")[0])

		for element in homepageHtml.xpath("//select[@id='skjzzc']/option"):
			self.model_.endWeekList_.append(element.text if element.text else "不限")
			self.model_.endWeekValueList_.append(element.xpath("./@value")[0])

		for element in homepageHtml.xpath("//select[@id='sksj']/option"):
			self.model_.dayList_.append(element.text if element.text else "不限")

		guiLogger.info("Successfully parsed options lists")

	def queryCourseList(self) -> None:
		guiLogger.info("Query course list")
		self.manager_.post(
			self.queryCourseListUrl_,
			self._setCourseList,
			None,
			{
				"page": self.model_.currentPage_,
				"kcmc": self.model_.courseName_ if self.model_.courseName_ else "",
				"jsxm": self.model_.teacherName_ if self.model_.teacherName_ else "",
				"kcfw": self.model_.majorRangeIndex_,
				"syxs": self.model_.studentTypeIndex_,
				"yxsh": self.model_.collegeValueList_[self.model_.collegeIndex_],
				"sxxsfl": "",
				"kkxq": self.model_.campusIndex_ if self.model_.campusIndex_ else "",
				"skqszc": self.model_.startWeekValueList_[self.model_.startWeekIndex_],
				"skjzzc": self.model_.endWeekValueList_[self.model_.endWeekIndex_],
				"sksj": self.model_.dayIndex_ if self.model_.dayIndex_ else "",
			},
			"application/x-www-form-urlencoded"
		)

	def _setCourseList(self, reply: QNetworkReply) -> None:
		self.model_.courseTableModel_.clear()
		self.model_.courseTableModel_.setHorizontalHeaderLabels(self.model_.courseTableHeaders_)
		courseList = json.loads(reply.readAll().data().decode())
		if courseList:
			for course in courseList:
				courseInfo = {
					"kcmc": course["kcmc"],
					"kcid": course["kcid"],
					"jtxh": course["jtxh"],
					"selected": course.get("xkjg") == "1",
					"selectable": course.get("xkjg") is None and course["sfkxk"] == "1",
					"droppable": course.get("xkjg") == "1" and course["sfktx"] == "1"
				}
				self.model_.courseInfoList_.append(courseInfo)
				self.model_.courseTableModel_.appendRow(
					[
						QStandardItem(course["kcmc"]),
						QStandardItem("选中" if courseInfo["selected"] else "未选中"),
						QStandardItem(course["xf"]),
						QStandardItem(str(course["ks"])),
						QStandardItem(course["jsxm"]),
						QStandardItem(f"[{course['yxsh']}]{course['yxmc']}"),
						QStandardItem(f"[{course['zydm']}]{course['zymc']}"),
						QStandardItem(course["sjms"]),
						QStandardItem(course["rnrs"]),
						QStandardItem(str(int(course["syrs"]))),
					]
				)
			self.model_.maxPage_ = courseList[0]["maxPage"]
		else:
			self.model_.maxPage_ = 1
		self.courseListUpdated.emit()
		guiLogger.info("Successfully set course list")
		reply.deleteLater()

	def operateCourse(self, isChooseCourse: bool, *args, **kwargs) -> None:
		"""
		Choose or drop selected course in courseTableView
		:param isChooseCourse: decide whether to choose or drop course
		:param args: tuple(courseName: str, show: bool). `courseName` is field `kcmc` in courseInfoDict. `show` decide whether to output to log or not.
		:param kwargs: dict{kkid: str, jtxh: str}. Fields in kwargs come from corresponding fields in courseInfoDict.
		:return: None
		"""
		if args[1]:
			guiLogger.info(f"{'Choose' if isChooseCourse else 'Drop'} selected course: {args[0]}")
		self.manager_.post(
			self.chooseCourseUrl_ if isChooseCourse else self.dropCourseUrl_,
			self._handleOperateCourse,
			None,
			kwargs,
			"application/x-www-form-urlencoded",
			True,
			*args
		)

	def _handleOperateCourse(self, reply: QNetworkReply, courseName: str, show: bool) -> None:
		resData = json.loads(reply.readAll().data().decode())
		if show:
			guiLogger.info(f"Course name: {courseName}, result: [{resData['code']}] {resData['msg']}")
		elif resData["code"] == 200:
			guiLogger.info(f"Successfully choose course: {courseName}")

	def addAutoCourse(self) -> None:
		if not self.model_.autoCourseTableModel_.columnCount():
			self.model_.autoCourseTableModel_.setHorizontalHeaderLabels(self.model_.courseTableHeaders_)
		rowItems = list()
		for colIdx in range(self.model_.courseTableModel_.columnCount()):
			rowItems.append(QStandardItem(self.model_.courseTableModel_.item(self.model_.selectedCourse_.row(), colIdx).text()))
		self.model_.autoCourseTableModel_.appendRow(rowItems)
		self.model_.autoCourseInfoList_.append(self.model_.courseInfoList_[self.model_.selectedCourse_.row()])
		guiLogger.info(f"Added selected course: {self.model_.autoCourseInfoList_[-1]['kcmc']}")

	def deleteAutoCourse(self) -> None:
		guiLogger.info(f"Deleted {len(self.model_.selectedAutoCourse_)} selected course(s)")
		for row in sorted(self.model_.selectedAutoCourse_, key=lambda x: x.row(), reverse=True):
			self.model_.autoCourseTableModel_.removeRow(row.row())
			self.model_.autoCourseInfoList_.pop(row.row())

	def clearAutoCourse(self) -> None:
		self.model_.autoCourseTableModel_.clear()
		self.model_.autoCourseInfoList_.clear()
		guiLogger.info("Cleared selected course(s)")

	def timerSwitch(self) -> None:
		if self.timer_.isActive():
			self.timer_.stop()
			guiLogger.info("Timer stopped")
		else:
			self.timer_.start(self.model_.timerInterval_)
			guiLogger.info(f"Timer started with interval: {self.model_.timerInterval_} ms")

	def _onTimerTimeout(self) -> None:
		autoCourseInfo = self.model_.autoCourseInfoList_[self.model_.autoCourseIndex_]
		self.operateCourse(
			True,
			autoCourseInfo["kcmc"],
			False,
			kkid=autoCourseInfo["kcid"],
			jtxh=autoCourseInfo["jtxh"]
		)
		self.model_.autoCourseIndex_ = (self.model_.autoCourseIndex_ + 1) % len(self.model_.autoCourseInfoList_)

	def _exit(self):
		self.manager_.get(
			f"{rootDomain}/casLogout"
		)
		guiLogger.info("Program exited")
