#import qgis files
from qgis.PyQt.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout
from qgis.PyQt import QtWidgets
from qgis.gui import QgsMapToolEdit


from SurveyPoint.ui.createPointsWindow import CreatePointsWindow
from SurveyPoint.ui.attributesWindow import AttributesWindow
from SurveyPoint.ui.databaseWindow import DatabaseWindow
        
class Create_points(QgsMapToolEdit):

    def __init__(self, canvas):
        super(Create_points, self).__init__(canvas)

    def create_pts(self):
        print('siema')

    def create_points_window(self):
        self.crt_pts_win = CreatePointsWindow()
        self.crt_pts_win.show()
        

class Attributes:

    def __init__(self):
        pass
    def attributes_window(self):
        self.crt_attrs_win = AttributesWindow()
        self.crt_attrs_win.show()


class Database:

    def __init__(self):
        pass

    def create_database(self):
        pass

    def database_window(self):
        self.crt_dtbs_win = DatabaseWindow()
        self.crt_dtbs_win.show()
        
    def add_to_database(self):
        pass

    def delete_from_database(self):
        pass
    
