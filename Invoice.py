import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PySide6.QtWebEngineWidgets import QWebEngineView
from jinja2 import Template
from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setWindowTitle("Invoice Generator")

        # Create button
        # self.save_button = QPushButton("Save PDF")
        # self.save_button.clicked.connect(self.save_pdf)

        # # Create layout and add button
        # layout = QVBoxLayout()
        # layout.addWidget(self.save_button)

        # # Create central widget and set layout
        # central_widget = QWidget()
        # central_widget.setLayout(layout)
        # self.setCentralWidget(central_widget)

    def save_pdf(self):
        # Your dynamic data
        data = {
            'date': datetime.now().strftime('%B %d, %Y'),
            'time': datetime.now().strftime('%H:%M:%S'),
            'invoice_number': '00123',
            'items': [
                {'name': 'Item A', 'quantity': 2, 'unit_price': '$10', 'amount': '$20'},
                {'name': 'Item B', 'quantity': 1, 'unit_price': '$20', 'amount': '$20'},
                {'name': 'Item C', 'quantity': 3, 'unit_price': '$15', 'amount': '$45'}
            ],
            'total': '$85'
        }

        # Read the HTML template
        with open('invoice_template.html', 'r') as file:
            template_content = file.read()

        # Create a Jinja2 template
        template = Template(template_content)

        # Render the template with dynamic data
        html_content = template.render(data)

        # Create a QWebEngineView to render HTML content
        webview = QWebEngineView()
        webview.setHtml(html_content)

        def on_load_finished(result):
            # Once the page is loaded, print it to a PDF file
            save_path, _ = QFileDialog.getSaveFileName(self, "Save PDF", "invoice.pdf", "PDF Files (*.pdf)")
            if save_path:
                webview.page().printToPdf(save_path)

        # Connect to the loadFinished signal to trigger saving PDF when the page is loaded
        webview.page().loadFinished.connect(on_load_finished)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
