import json
from lxml import etree

from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QModelIndex, QSortFilterProxyModel
from PySide6.QtNetwork import QNetworkReply


class MainWindowModel:
	def __init__(self):
		self.majorRangeList_: list[str] = list()
		self.studentTypeList_: list[str] = list()
		self.campusList_: list[str] = list()
		self.collegeList_: list[str] = list()
		self.startWeekList_: list[str] = list()
		self.endWeekList_: list[str] = list()
		self.dayList_: list[str] = list()

		self.collegeValueList_: list[str] = list()
		self.startWeekValueList_: list[str] = list()
		self.endWeekValueList_: list[str] = list()

		self.courseInfoList_: list[dict[str, str | bool]] = list()
		self.autoCourseInfoList_: list[dict[str, str | bool]] = list()

		self.logPlainEditMaxBlockCount_: int = 50
		self.timerInterval_: int = 200
		self.autoCourseIndex_: int = 0

		self.majorRangeIndex_: int = 0
		self.studentTypeIndex_: int = 0
		self.campusIndex_: int = 0
		self.collegeIndex_: int = 0
		self.startWeekIndex_: int = 0
		self.endWeekIndex_: int = 0
		self.dayIndex_: int = 0
		self.courseName_: str = str()
		self.teacherName_: str = str()

		self.currentPage_: int = 1
		self.maxPage_: int = 1

		self.courseTableModel_: QStandardItemModel = QStandardItemModel()
		self.courseTableProxyModel_: QSortFilterProxyModel = QSortFilterProxyModel()
		self.autoCourseTableModel_: QStandardItemModel = QStandardItemModel()
		self.courseTableHeaders_: list[str] = ["课程名称", "选中状态", "学分", "总课时", "任课教师", "开课院系", "专业名称", "上课时间", "容纳人数", "剩余人数（仅供参考）"]

		self.selectedCourse_: QModelIndex = QModelIndex()
		self.selectedAutoCourse_: list[QModelIndex] = list()

		self.courseTableProxyModel_.setSourceModel(self.courseTableModel_)
