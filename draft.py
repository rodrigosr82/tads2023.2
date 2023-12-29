import plotly.express as px

from data.download import download_data

data = download_data('CPLE3.SA')

data[['Close']]
data['SMA']= data['Close'].rolling(window = 9).mean()
data['LMA']= data['Close'].rolling(window = 72).mean()

px.line(
    data.reset_index(),
    x='Date', y=['Close', 'SMA','LMA'], title='CPLE3.SA',
    labels={'Close':'Fechamento', 'Date':'Data'},
    color_discrete_map= {'Close': 'black', 'SMA': 'blue', 'LMA': 'red'}
)


###plot_line_i('BBAS3.SA', 'CPLE3.SA')


