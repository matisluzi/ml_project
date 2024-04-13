from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QComboBox, QLabel
import pandas as pd


class MyApp(QWidget):

    data = None

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CIS4930 Project')
        self.move(300, 300)
        self.resize(400, 500)

        # drop down menu: region name
        region_name_label = QLabel('Region Name', self)
        region_name_label.move(20, 20)
        region_name_label.resize(200, 30)

        region_name = QComboBox(self)
        for region in self.data['RegionName']:
            region_name.addItem(region)
        region_name.move(20, 50)
        region_name.resize(300, 30)

        # text fields: no of bedrooms, planned price of buying, date
        no_of_bedrooms = QLineEdit(self)
        no_of_bedrooms.move(20, 100)
        no_of_bedrooms.resize(200, 30)
        no_of_bedrooms.setPlaceholderText('Number of Bedrooms')

        planned_price = QLineEdit(self)
        planned_price.move(20, 150)
        planned_price.resize(200, 30)
        planned_price.setPlaceholderText('Your price')

        date = QLineEdit(self)
        date.move(20, 200)
        date.resize(200, 30)
        date.setPlaceholderText('Date')

        # button: submit
        btn = QPushButton('Submit', self)
        btn.move(20, 250)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(lambda: self.buttonClicked(region_name.currentText(), no_of_bedrooms.text(),
                                                       planned_price.text(), date.text()))

        # label for error message, shown when fields are not filled correctly
        self.error_label = QLabel('', self)
        self.error_label.move(20, 300)
        self.error_label.resize(200, 30)
        self.error_label.setStyleSheet('color: red')

        self.show()

    def buttonClicked(self, region_name, no_of_bedrooms, planned_price, date):
        # check if all fields are filled
        if not region_name or not no_of_bedrooms or not planned_price or not date:
            self.error_label.setText('Please fill all fields')
            return

        # check if number of bedrooms is a number
        try:
            no_of_bedrooms = int(no_of_bedrooms)
        except ValueError:
            self.error_label.setText('Number of bedrooms must be a number')
            return

        # check if planned price is a number
        try:
            planned_price = int(planned_price)
        except ValueError:
            self.error_label.setText('Planned price must be a number')
            return

        # check if date is in the format YYYY-MM
        if len(date) != 7 or date[4] != '-':
            self.error_label.setText('Date must be in the format YYYY-MM')
            return

        print(region_name, no_of_bedrooms, planned_price, date)


def readData():
    data = pd.read_csv('Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_month.csv')
    return data


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    metro_data = readData()
    ex = MyApp(metro_data)
    sys.exit(app.exec_())
