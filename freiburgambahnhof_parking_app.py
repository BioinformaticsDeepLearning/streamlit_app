# Import modules
#from parkwhere import extract_all_features
import streamlit as st
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pickle as pkl
import plotly.graph_objects as go
import seaborn as sns
import plotly.express as px
loaded_model = pkl.load(open("park_where_mdl_final.pkl", "rb"))

def main():
    import plotly.express as px
    #fig, axs = plt.subplots(2,2, figsize=(15, 6), facecolor='w', edgecolor='k')
    #fig.subplots_adjust(hspace = .5, wspace=.001)
    #axs = axs.ravel()
    # for i in range(10):


        
    def Probabilty_Date_Range(date,dow,starting_time,ending_time,holiday):
        minutes_range = list(range(0,60,15))
        output = []
        for n,minute in enumerate(minutes_range):
            
            output = []
            input = [date[0],date[1],date[2],dow,starting_time,minute,0,holiday]
    #         print(input)
            output = loaded_model.predict_proba([input])
            #st.write(output[0][0])
            #st.write(output[0][1]) 
            data = [output[0][0], output[0][1]]
            label = ['No', 'Yes']

            st.write("Yes ---  % Probability of Garage less than 100")
            st.write(" No  ---  % Probability of Garage is 100 or more than 100")

            x=label
            y=data
            fig,ax=plt.subplots()
            ax.pie(y,labels=x,autopct="%0.2f")
            plt.xticks(rotation='vertical')
            plt.title('At time '+str(starting_time)+str(' : ')+str(minute)+str(' to ')+str(starting_time)+str(' : ')+str(minute+15))
            st.pyplot(fig)



            x =n
            #fig,ax=plt.subplots()
            #fig, axs = plt.subplots(2,2, figsize=(15, 6), facecolor='w', edgecolor='k')
            #plt.subplot(2, 2,x+1)
            #axs[x].pie(data, labels=label, autopct='%1.1f%%', shadow=True, startangle=90)
            #st.pyplot(fig)
            if n==0:
                l=[""*15,starting_time,":0",minute+1,"to",starting_time,":",minute+15,""*15]
                #st.write(l)
            else:
                l=[""*15,starting_time,":",minute+1,"to",starting_time,":",minute+15,""*15]
    #         axs[n].contourf(np.random.rand(10,10),5,cmap=plt.cm.Oranges)
                #axs[x].set_title(str("  ".join(map(str, l))))
    #         plt.title('parking')
    #         plt.axis('equal')
    #         plt.show()
            
    #         break
    # day of week is 2 Tuesday 



    # Main interface
    st.title("Freiburgambahnhof Parking System")


    # Get date and time inputs (defaults to current date and time)
    input_date =st.date_input('Enter date...', dt.date.today(), key='1') 
    col1,col2=st.columns(2)
    with col1:
        st.write("Start Time -- HH")
        strt_time=st.text_input("Enter Start Time",value="00")
    with col2:
        st.write("End Time -- HH")
        end_time=st.text_input("Enter End Time",value="00")

    
    col1,col2=st.columns(2)
    days_of_week={"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}


    with col1:
        selected_day=st.selectbox("Select the Day",days_of_week.keys())
    with col2:
        st.write("")
        st.write("")
        st.write("")
        holiday=st.checkbox("Holiday")
    st.write("")
    st.write("")
    st.write("")
    year,mnth,day=str(input_date).split("-")
    if holiday=="True":
        holiday=1
    else:
        holiday=0
    col1,col2,col3,col4,col5=st.columns(5)
    
    #input_parameters=[int(year),int(mnth),int(day),days_of_week[selected_day],strt_time,15,0,holiday]
    
    #with col3:
    if  st.button("Predict"):
        st.write("")
        st.write("")
        st.write("")
        st.subheader("Results")
        st.write("")
        st.write("")
        st.write("")
        Probabilty_Date_Range([int(year),int(mnth),int(day)],days_of_week[selected_day],strt_time,end_time,holiday)
    #    results=loaded_model.predict_proba([input_parameters])
     #   plot={"Yes":results[0][0],"No":results[0][1]}
      #  st.write("Yes ---  % Probability of Garage less than 100")
       # st.write(" No  ---  % Probability of Garage is 100 or more than 100")
        #x=plot.keys()
        #y=plot.values()
        #fig,ax=plt.subplots()
        #ax.pie(y,labels=x,autopct="%0.2f")
        #plt.xticks(rotation='vertical')
        #st.pyplot(fig)
        pass
   # time_now_predict = dt.datetime.now() + dt.timedelta(hours=8) # Based on server time
    # time_now_predict = dt.datetime.now() # Based on local machine time
#    time_now_predict = time_now_predict.strftime("%H:%M")
 #   time_now_predict = p2.text_input("... and time", value=time_now_predict, key='1') 

    # Load trained model
  
    #model = pkl.load(open(filename))
    #model = pickle.load(open('./Data_Analytics_Projects/Data_Analysis_Projects/Numerical Data Analytics/New Folder/finalized_model.sav', 'rb'))
    #Arrange date and time inputs as a DataFrame and extract features
    

    

if __name__ == "__main__":
    main()
