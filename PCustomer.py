import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
import datetime as dt
from PIL import Image

dfbefore = pd.read_csv(r'customer_shopping_data.csv')
df = pd.read_csv(r'NewData.csv')
st.set_page_config(layout='wide' )

# sidebar
st.sidebar.header('Choose Page')
st.sidebar.subheader('Each page has different options')
option = st.sidebar.selectbox(
    "Select an option",
    ["Home",
     "Data Attributes",
     "Univariate Analysis",
     'Bivariate  & Multivariate Analysis'
    ]
)

if option == 'Home':
    st.write('Author : @MostafaAbdelbadie')
    st.write('Linkdin : https://www.linkedin.com/in/mostafa-abdelbadie')
    st.write('Whatsapp Number : (+20) 1142359150')
    st.title('Customer Shopping EDA')
    st.write('- <p style="font-size:26px;">This is a EDA project Made by Mostafa Abdelbadie with python codes for customers shopping data in Turkey. This data is from Kaggle .Dataset contains shopping information from 10 different shopping malls between 2021 and 2023. The dataset includes essential information such as invoice numbers, customer IDs, age, gender,payment methods, product categories, quantity, price, order dates, and shopping mall locations</p>',
unsafe_allow_html=True)
    st.write('- <p style="font-size:26px;"> Feel free to contact me to recieve the dataset & python notebook</p>',
unsafe_allow_html=True)

    image =Image.open(r'Pimage.png')
    coll1, coll2, coll3 = st.columns([3,6,1])

    with coll1:
            st.write("     ")

    with coll2:
            st.image(image , width= 700)
            

    with coll3:
            st.write("")
            
        
if option == 'Data Attributes':
    ## Data Preview
    st.header('Data Before Cleanning')
    st.dataframe(dfbefore.head(10))
    st.header('Attrbuites Info')
    st.write('- Invoice_no: Invoice number. Nominal. A combination of the letter ''I'' and a 6-digit integer uniquely assigned to each operation.')
    st.write('- Customer_id: Customer number. Nominal. A combination of the letter ''C'' and a 6-digit integer uniquely assigned to each operation.')
    st.write('- Gender: String variable of the customer gender.')
    st.write('- Age: Positive Integer variable of the customers age.')
    st.write('- Quantity: The quantities of each product (item) per transaction. Numeric.')
    st.write('- Price: Unit price. Numeric. Product price per unit in Turkish Liras (TL).')
    st.write('- Payment_method: String variable of the payment method (cash, credit card or debit card) used for the transaction')
    st.write('- Invoice_date: Invoice date. The day when a transaction was generated.')
    st.write('- Shopping_mall: String variable of the name of the shopping mall where the transaction was made.')

    st.header('Data Cleanning Steps')
    st.write('To be Able to analysis the data effciently I added Columns')
    st.write('Age_Range , Day , Month , Year')
    st.dataframe(df.head(10))

if option == 'Univariate Analysis':
    st.subheader('Univariate Analysis')
    col1 , col2 = st.columns(2)
    with col1:
        st.write('- Which Gender has the highest Percentage Purchasing')
        fig=px.bar(data_frame = df ,
                    x = df['Gender'].value_counts().index
                    ,y = df['Gender'].value_counts().values
                    )
        fig.update_xaxes(title='Gender')
        fig.update_yaxes(title='Total Number')
        fig.update_traces(marker_color='lightsalmon')
        st.plotly_chart(fig)
    with col2:
            st.write('- What are The percentages or Distrbution of Ages?')
            fig2=px.pie(data_frame = df,
            names= df['Age_Range'].value_counts().sort_index().index,
            values= df['Age_Range'].value_counts().sort_index().values,
            title = 'Ages of All Customers ',
            hole = 0.5)
            st.plotly_chart(fig2)
    co1 , co2 , co3 = st.columns([3,7,3])
    with co1:
            st.write("     ")

    with co2:
        option1 = st.selectbox(
        "Select an Something to be presented with Bar Chart",
        ['Category'
         ,'Shopping_mall'
         ,'Payment_method'])
        fig3=px.bar(data_frame= df , x =option1)
        st.plotly_chart(fig3)    
    with co3:
            st.write("")

if option == 'Bivariate  & Multivariate Analysis':
    st.subheader('Bivariate  & Multivariate Analysis')
    
    c1 , c2 = st.columns(2)
    with c1:
        st.write('- <p style="font-size:19px;"> what are the categories with highest purchases Across (Age Range / Gender)</p>'
        ,unsafe_allow_html=True)
        option2 = st.selectbox(
        '',
        ['Gender',
         'Age_Range']
        )
        df1=df.groupby(['Gender','Age_Range'])['Category'].value_counts().to_frame()
        df1.rename(columns=({'Category':'Total'}),inplace=True)
        df1=df1.reset_index()
        
        fig4= px.bar( df1 , x=df1['Category'] ,
            y= df1['count']
        , color= option2
        , barmode = 'group')
        fig4.update_xaxes(title='Categories ')
        fig4.update_yaxes(title='Total Sales')
        st.plotly_chart(fig4)
        st.write('- <p style="font-size:19px;"> Average Total Payment by each Gender </p>',
        unsafe_allow_html=True)
        fig6=px.box(df , x='Total_payment' , color='Gender')
        st.plotly_chart(fig6)
    with c2:
        st.write('- <p style="font-size:19px;"> Paymment Method Across (Age Range / Gender) </p>'
        ,unsafe_allow_html=True)
        option3 = st.selectbox(
        ' ',
        ['Age_Range',
         'Gender']
        )
        df2 =df.groupby(['Age_Range','Gender'])['Payment_method'].value_counts().to_frame()
        df2.rename(columns={'Payment_method':'Total'}, inplace = True)
        df2 = df2.reset_index()
        fig5= px.bar( df2 , x=(df2[option3]) ,
           y= df2['count']
        , color='Payment_method'
        , barmode = 'group')
        fig5.update_xaxes(title=option3)
        fig5.update_yaxes(title='Total')
        st.plotly_chart(fig5)
        st.write('- <p style="font-size:19px;"> Average total bill for each Cateogry </p>'
        ,unsafe_allow_html=True)
        fig7=px.box(df , y= 'Price', color='Category')
        st.plotly_chart(fig7)
    K1 , K2 = st.columns(2)
    with K1:
            st.write('- <p style="font-size:19px;"> Performance Of malls across all years </p>'
            ,unsafe_allow_html=True)
            df4 =df.groupby(['MonthNo',
                             'Month',
                             'Year'])['Total_payment'].sum().reset_index()
            fig8=px.line(df4 , x=['Month','Year'] , y='Total_payment' , color='Year')
            st.plotly_chart(fig8)
    with K2:
        st.write('-  <p style="font-size:19px;"> Perforamce Of each Mall across years</p>'
                 ,unsafe_allow_html=True)
        df5 =df.groupby(['MonthNo',
                         'Month',
                         'Shopping_mall',
                         'Year'])['Total_payment'].sum().reset_index()
        fig9=px.bar(df5 , x='Year' , y='Total_payment' , 
        color='Shopping_mall'
        ,barmode='group')
        st.plotly_chart(fig9)
        

            
            
