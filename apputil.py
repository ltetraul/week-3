import seaborn as sns
import pandas as pd

#exercise 1
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
print(fib(10))

#exercise 2
def to_binary(n):
    if n < 2:
        return str(n)
    else:
        return to_binary(n // 2) + str(n % 2)
print(to_binary(2))
print(to_binary(15))

#exercise 3
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

def task_1(df):
    #fix gender column
    if 'gender' in df.columns:
        df['gender'] = df['gender'].replace(r'^\s*$', pd.NA, regex=True)
    return df.isnull().sum().sort_values(ascending=False)

def task_2(df):
    #admissions per year dataframe
    if 'year' not in df.columns:
        return pd.DataFrame(columns=['year', 'total_admissions'])
    return df.groupby('year').size().reset_index(name='total_admissions')

def task_3(df):
    #series of average age by gender
    if 'gender' not in df.columns or 'age' not in df.columns:
        return pd.Series(dtype=float)
    return df.dropna(subset=['gender', 'age']).groupby('gender')['age'].mean()

def task_4(df):
    #list of top 5 professions
    if 'profession' not in df.columns:
        return []
    return df['profession'].value_counts().head(5)

