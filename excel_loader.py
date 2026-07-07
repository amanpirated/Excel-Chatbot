import pandas as pd 
import os
class ExcelLoader:
    def __init__(self,file_path=None):
        # use provided file_path, fallback to default if None 
        if file_path is None:
            base_dir=os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )
            file_path=os.path.join(
                base_dir,
                "data",
                "Employee Sample Data.xlsx"
            )
        self.file_path =  r"C:\Users\Admin\project2\data\Employee Sample Data.xlsx"
    def load_excel(self):
        """Load Excel file and return a DataFrame."""
        if not os.path.exists(self.file_path):

            raise FileNotFoundError(
                f"File not found: {self.file_path}"
            )
        df = pd.read_excel(self.file_path) 
        return df