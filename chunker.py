import pandas as pd 
class Chunker:
    def __init__(self,dataframe):
        self.df=dataframe
    
    def create_chunks(self):
        #This function converts the DataFrame into text chunks.
        chunks=[]
        grouped=self.df.groupby("Department")
        for department ,group in grouped:
            text=f"""
Department: {department}
Employee Records
{group.to_string(index=False)}"""
            
            chunk={
                "text":text,
                "metadata":{
                    "department":department,
                    "rows":len(group)
                }
            }

            chunks.append(chunk)
        return chunks