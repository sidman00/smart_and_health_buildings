from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
def create_data_file(co2_file,lux_file,data_list,output_file):
    co2_file = open(co2_file,'r')
    lux_file = open(lux_file,'r')
    output_file = open(output_file,'a')
    co2_file.readline()
    lux_file.readline()
    for i in range(0,5):
        current_productivity_value = data_list[i]
        for j in range(0,60):
            current_co2_data = co2_file.readline().rstrip().split(',')
            current_lux_data = lux_file.readline().rstrip().split(',')
            output_file.write(str(current_co2_data[-1])+','+str(current_lux_data[-1])+','+str(current_productivity_value)+'\n')
    co2_file.close()
    lux_file.close()
    output_file.close()


def create_project_data_file():
    data_file = open('project_data.csv','w')
    data_file.write('co2,lux,productivity')
    data_file.close()
    create_data_file('co2_120_day1.csv','lux_120.csv',[0.8824,0.7917,0.8723,0.9184,0.9583],'project_data.csv')
    create_data_file('co2_120_day2.csv','lux_120.csv',[0.9286,0.8929,0.9464,1.00,1.00],'project_data.csv')
    create_data_file('co2_005_day_1.csv','lux_005_day_1.csv',[0.7368,0.8684,0.8158,0.8158,0.8158],'project_data.csv')
    create_data_file('co2_005_day_2.csv','lux_005_day_2.csv',[0.9592,0.8723,0.8679,0.9333,0.9074],'project_data.csv')

def learn(data_file):
    data = open(data_file,'r')
    data.readline()
    X_data = []
    Y_data = []
    for line in data:
        current_data = line.lstrip().rstrip().split(',')
        X_data.append([float(current_data[0]),float(current_data[1])])
        Y_data.append(float(current_data[-1]))
    X_train, X_test, y_train, y_test = train_test_split(X_data, Y_data, test_size=0.2, random_state=0)
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))

# create_project_data_file()
learn('project_data.csv')


