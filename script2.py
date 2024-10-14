import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

income = np.array([93.62,91.54,93.25,94.164,96.12,102.89,105.27,108.963,112.256,119.32,125.89,127.914])
income_without_tax = income * .7
expenses = np.array([76.02, 76.75,77.662,79.25,82.56, 84.094,90.44,96.78,103.209,107.89,111.64,114.884])

fin_res = pd.DataFrame(
    data = {'Income_without_tax': income_without_tax, 'Expenses' : expenses})
fin_res['Month'] = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September', 'October', 'November', 'December' ]
months = {
    'January' : 1,
    'February' : 1,
    'March' : 1,
    'April' : 2,
    'May' : 2,
    'June' : 2,
    'July' : 3,
    'August' : 3,
    'September' : 3,
    'October' : 4,
    'November' : 4,
    'December' : 4
}
fin_res['Quarter'] = fin_res['Month'].map(months)
q1 = fin_res[fin_res['Quarter'] == 1]

print(fin_res,'\n', q1)