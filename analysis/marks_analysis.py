import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('marks.csv')
print("Student Marks Data:")
print(df)

for subject in ['maths', 'physics', 'chemistry']:
    avg = df[subject].mean()
    print(f"Average marks in {subject}: {avg:.2f}")

plt.figure(figsize=(10, 6))
for subject in ['maths', 'physics', 'chemistry']:
    plt.bar(df['name'], df[subject], alpha=0.6, label=subject)

plt.xlabel('Student')
plt.ylabel('Marks')
plt.title('Marks of Students by Subject')
plt.xticks(rotation=45)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
chart_path = 'marks_chart.png'
plt.savefig(chart_path)
print(f"\nChart saved at: {os.path.abspath(chart_path)}")
plt.show()
