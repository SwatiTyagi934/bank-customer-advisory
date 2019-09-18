def balance(x):
    if x < 1 :
        return 0
    if x >= 1 and x < 500000 :
        return 1
    if x >= 500000 and x < 1500000 :
        return 2
    if x >= 1500000 and x < 3000000 :
        return 3
    if x >= 3000000 and x < 5000000 :
        return 4
    if x >= 5000000 and x < 10000000 :
        return 5
    if x >= 10000000 and x < 15000000 :
        return 6
    if x >= 15000000 and x < 50000000 :
        return 7
    if x >=50000000 :
        return 8
def age(x):
    if x < 19 :
        return 0
    if x >= 19 and x < 26 :
        return 1
    if x >= 26 and x < 35 :
        return 2
    if x >= 35 and x < 50 :
        return 3
    if x >= 50 and x < 60 :
        return 4
    if x >= 60 and x < 75 :
        return 5
    if x >= 75 :
        return 6
def job(x):
    if x == 'management':
        return 1
    if x == 'technician':
        return 1
    if x == 'entrepreneur':
        return 4
    if x == 'blue':
        return 5
    if x == 'unknown':
        return 0
    if x == 'retired':
        return 3
    if x == 'admin':
        return 1
    if x == 'services':
        return 1
    if x == 'self':
        return 4
    if x == 'unemployed':
        return 2
    if x == 'housemaid':
        return 5
    if x == 'student':
        return 2
def marital(x):
    if x == 'married':
        return 0
    if x == 'single':
        return 1
    if x == 'divorced':
        return 2
def education(x):
    if x == 'tertiary':
        return 0
    if x == 'secondary':
        return 1
    if x == 'unknown':
        return 2
    if x == 'primary':
        return 3
def default(x):
    if x == 'yes':
        return 0
    if x == 'no':
        return 1
def housing(x):
    if x == 'yes':
        return 0
    if x == 'no':
        return 1
def loan(x):
    if x == 'yes':
        return 0
    if x == 'no':
        return 1

def applyall(df):
    df.loan=df.loan.apply(loan)
    df.balance=df.balance.apply(balance)
    df.housing=df.housing.apply(housing)
    df.default=df.default.apply(default)
    df.education=df.education.apply(education)
    df.marital=df.marital.apply(marital)
    df.age=df.age.apply(age)
    df.job=df.job.apply(job)
    return df