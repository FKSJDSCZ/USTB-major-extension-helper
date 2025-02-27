from PySide6.QtCore import QObject, QModelIndex
from PySide6.QtWidgets import QHeaderView

from model.MainWindowModel import MainWindowModel
from service.MainWindowService import MainWindowService
from view.MainWindowView import MainWindowView


class MainWindowController(QObject):
	def __init__(self, mainWindowView: MainWindowView, mainWindowService: MainWindowService, mainWindowModel: MainWindowModel, /):
		super().__init__()
		self.view_: MainWindowView = mainWindowView
		self.service_: MainWindowService = mainWindowService
		self.model_: MainWindowModel = mainWindowModel

		self._modelBindInit()
		self._connectionInit()

	def _modelBindInit(self) -> None:
		self.view_.mainWindow_.courseTableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
		self.view_.mainWindow_.autoCourseTableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
		self.view_.mainWindow_.courseTableView.setModel(self.model_.courseTableProxyModel_)
		self.view_.mainWindow_.autoCourseTableView.setModel(self.model_.autoCourseTableModel_)

	def _connectionInit(self) -> None:
		# from view
		self.view_.mainWindow_.queryBtn.clicked.connect(self._onQueryBtnClicked)
		self.view_.mainWindow_.resetBtn.clicked.connect(self._onResetBtnClicked)
		self.view_.mainWindow_.firstPageBtn.clicked.connect(lambda: self._onChangePage(1))
		self.view_.mainWindow_.previousPageBtn.clicked.connect(lambda: self._onChangePage(self.model_.currentPage_ - 1))
		self.view_.mainWindow_.nextPageBtn.clicked.connect(lambda: self._onChangePage(self.model_.currentPage_ + 1))
		self.view_.mainWindow_.lastPageBtn.clicked.connect(lambda: self._onChangePage(self.model_.maxPage_))
		self.view_.mainWindow_.jumpPageBtn.clicked.connect(lambda: self._onChangePage(self.view_.mainWindow_.pageSpinBox.value()))
		self.view_.mainWindow_.operateCourseBtn.clicked.connect(self._onOperateCourseBtnClicked)
		self.view_.mainWindow_.addAutoBtn.clicked.connect(self.service_.addAutoCourse)
		self.view_.mainWindow_.delAutoBtn.clicked.connect(self.service_.deleteAutoCourse)
		self.view_.mainWindow_.switchAutoBtn.clicked.connect(self._onSwitchAutoBtnClicked)
		self.view_.mainWindow_.clearAutoBtn.clicked.connect(self.service_.clearAutoCourse)

		self.view_.mainWindow_.courseTableView.clicked.connect(self._onCourseTableClicked)
		self.view_.mainWindow_.autoCourseTableView.clicked.connect(self._onAutoCourseTableClicked)

		self.view_.exitMsgBox_.accepted.connect(self._onExit)

		# from service
		self.service_.courseListUpdated.connect(self._onCourseListUpdated)

	def viewInit(self, htmlString: str) -> None:
		self.service_.getOptions(htmlString)
		self.view_.mainWindow_.majorRangeBox.addItems(self.model_.majorRangeList_)
		self.view_.mainWindow_.studentTypeBox.addItems(self.model_.studentTypeList_)
		self.view_.mainWindow_.campusBox.addItems(self.model_.campusList_)
		self.view_.mainWindow_.collegeBox.addItems(self.model_.collegeList_)
		self.view_.mainWindow_.startWeekBox.addItems(self.model_.startWeekList_)
		self.view_.mainWindow_.endWeekBox.addItems(self.model_.endWeekList_)
		self.view_.mainWindow_.dayBox.addItems(self.model_.dayList_)
		self.view_.show()

	def _onQueryBtnClicked(self) -> None:
		self.model_.majorRangeIndex_ = self.view_.mainWindow_.majorRangeBox.currentIndex()
		self.model_.studentTypeIndex_ = self.view_.mainWindow_.studentTypeBox.currentIndex()
		self.model_.campusIndex_ = self.view_.mainWindow_.campusBox.currentIndex()
		self.model_.collegeIndex_ = self.view_.mainWindow_.collegeBox.currentIndex()
		self.model_.startWeekIndex_ = self.view_.mainWindow_.startWeekBox.currentIndex()
		self.model_.endWeekIndex_ = self.view_.mainWindow_.endWeekBox.currentIndex()
		self.model_.dayIndex_ = self.view_.mainWindow_.dayBox.currentIndex()
		self.model_.courseName_ = self.view_.mainWindow_.courseNameEdit.text()
		self.model_.teacherName_ = self.view_.mainWindow_.teacherNameEdit.text()
		self.model_.currentPage_ = 1
		self.service_.queryCourseList()

	def _onResetBtnClicked(self) -> None:
		self.view_.mainWindow_.majorRangeBox.setCurrentIndex(0)
		self.view_.mainWindow_.studentTypeBox.setCurrentIndex(0)
		self.view_.mainWindow_.campusBox.setCurrentIndex(0)
		self.view_.mainWindow_.collegeBox.setCurrentIndex(0)
		self.view_.mainWindow_.startWeekBox.setCurrentIndex(0)
		self.view_.mainWindow_.endWeekBox.setCurrentIndex(0)
		self.view_.mainWindow_.dayBox.setCurrentIndex(0)
		self.view_.mainWindow_.courseNameEdit.clear()
		self.view_.mainWindow_.teacherNameEdit.clear()
		self._onQueryBtnClicked()

	def _onChangePage(self, page: int) -> None:
		self.model_.currentPage_ = page
		self.service_.queryCourseList()

	def _onOperateCourseBtnClicked(self) -> None:
		courseInfo = self.model_.courseInfoList_[self.model_.selectedCourse_.row()]
		self.service_.operateCourse(not courseInfo["selected"], kkid=courseInfo["kcid"], jtxh=courseInfo["jtxh"])

	def _onSwitchAutoBtnClicked(self) -> None:
		if self.model_.autoCourseInfoList_:
			self.model_.autoCourseIndex_ = 0
			text = self.view_.mainWindow_.switchAutoBtn.text()
			text = ("停止" if text[0:2] == "开始" else "开始") + text[2:]
			self.view_.mainWindow_.switchAutoBtn.setText(text)
			self.service_.timerSwitch()
		else:
			print("选课列表为空")

	def _onCourseTableClicked(self, index: QModelIndex) -> None:
		self.model_.selectedCourse_ = self.model_.courseTableProxyModel_.mapToSource(index)
		courseInfo = self.model_.courseInfoList_[self.model_.selectedCourse_.row()]
		self.view_.mainWindow_.operateCourseBtn.setText("退选课程" if courseInfo["selected"] else "选择课程")
		self.view_.mainWindow_.operateCourseBtn.setEnabled(courseInfo["selectable"] or courseInfo["droppable"])
		self.view_.mainWindow_.addAutoBtn.setDisabled(courseInfo["selected"])

	def _onAutoCourseTableClicked(self) -> None:
		self.model_.selectedAutoCourse = self.view_.mainWindow_.autoCourseTableView.selectionModel().selectedRows()

	def _onExit(self) -> None:
		self.view_.close()

	def _onCourseListUpdated(self) -> None:
		self.view_.mainWindow_.currentPageLabel.setText(str(self.model_.currentPage_))
		self.view_.mainWindow_.maxPageLabel.setText(str(self.model_.maxPage_))
		self.view_.mainWindow_.firstPageBtn.setDisabled(self.model_.currentPage_ == 1)
		self.view_.mainWindow_.previousPageBtn.setEnabled(self.model_.currentPage_ > 1)
		self.view_.mainWindow_.nextPageBtn.setEnabled(self.model_.maxPage_ > self.model_.currentPage_)
		self.view_.mainWindow_.lastPageBtn.setDisabled(self.model_.currentPage_ == self.model_.maxPage_)
		self.view_.mainWindow_.pageSpinBox.setMaximum(self.model_.maxPage_)
		self.view_.mainWindow_.operateCourseBtn.setDisabled(True)
		self.view_.mainWindow_.addAutoBtn.setDisabled(True)
