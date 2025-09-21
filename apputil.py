import seaborn as sns
import pandas as pd

#exercise 1
def fib(n):
    """
    Recursively compute the nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
        
print(fib(10)) #test example

#exercise 2
def to_binary(n):
    """
    Convert an integer to its binary representation as a string.
    """
    if n < 2:
        return str(n)
    else:
        return to_binary(n // 2) + str(n % 2)

print(to_binary(2))   #output should be 10
print(to_binary(15))  #output should be 1111

#exercise 3
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

def task_1(df):
    """
    Clean gender column and return count of missing values per column.
    """
    if 'gender' in df.columns:
        df['gender'] = df['gender'].replace(
            [r'^\s*$', r'^\?$', r'^[ghGH]$'],
            pd.NA,
            regex=True
        ) #fix blank entries, "?", "g", "h" characters by replacing them with NaN
    return df.isnull().sum().sort_values(ascending=False)


def task_2(df):
    """
    Create a dataframe of admissions per year.
    """
    if 'date_in' not in df.columns:
        return pd.DataFrame(columns=['year', 'total_admissions'])
    
    #convert date_in to datetime and extract year
    df['year'] = pd.to_datetime(df['date_in'], errors='coerce').dt.year
    return df.groupby('year').size().reset_index(name='total_admissions')


def task_3(df):
    """
    Calculate the average age grouped by gender.
    """
    if 'gender' not in df.columns or 'age' not in df.columns:
        return pd.Series(dtype=float)
    return df.dropna(subset=['gender', 'age']).groupby('gender')['age'].mean()


def task_4(df):
    """
    List the top 5 professions after formatting.
    """
    if 'profession' not in df.columns:
        return []
    
    #normalize professions
    df['profession'] = df['profession'].astype(str).str.lower().str.strip()
    return df['profession'].value_counts().head(5)

# run tasks
print(task_1(df_bellevue))
print(task_2(df_bellevue))
print(task_3(df_bellevue))
print(task_4(df_bellevue))
