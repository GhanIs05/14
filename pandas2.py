import pandas as pd
import numpy as np
# Sample dictionary data
exam_data = {
'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',
'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
# Index labels
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# Create a DataFrame
df = pd.DataFrame(exam_data, index=labels)
# Select rows where attempts < 2 and score > 15
selected_rows = df[(df['attempts'] < 2) & (df['score'] > 15)]
# Display the selected rows
print("Selected Rows:")
print(selected_rows)
