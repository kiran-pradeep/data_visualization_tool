import matplotlib.pyplot as plt


def bar_plot():
    plt.figure(figsize=(10,6))
    plt.bar([0.25,2.25,3.25,5.25,7.25],[300,400,200,600,700],
    label="Carpenter",color='b',width=0.5)
    plt.bar([0.75,1.75,2.75,3.75,4.75],[50,30,20,50,60],
    label="Plumber", color='g',width=.5)
    plt.legend()
    plt.xlabel('Days')
    plt.ylabel('Wage')
    plt.title('Details')

    plt.savefig("output2.png", bbox_inches='tight')



def scatter_plot():
    plt.figure(figsize=(10,6))

    x1 = [1, 2.5,3,4.5,5,6.5,7]
    y1 = [1,2, 3, 2, 1, 3, 4]
    x2=[8, 8.5, 9, 9.5, 10, 10.5, 11]
    y2=[3,3.5, 3.7, 4,4.5, 5, 5.2]
    plt.scatter(x1, y1, label = 'high bp low heartrate', color='c')
    plt.scatter(x2,y2,label='low bp high heartrate',color='g')
    plt.title('Smart Band Data Report')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

    plt.savefig("output2.png", bbox_inches='tight')


def pie_plot():
    plt.figure(figsize=(10,6))

    slice = [12, 25, 50, 36, 19]
    activities = ['NLP','Neural Network', 'Data analytics', 'Quantum Computing', 'Machine Learning']
    cols = ['r','b','c','g', 'orange']
    plt.pie(slice,
    labels =activities,
    colors = cols,
    startangle = 90,
    shadow = True,
    explode =(0,0.1,0,0,0),
    autopct ='%1.1f%%')
    plt.title('Training Subjects')

    plt.savefig("output2.png", bbox_inches='tight')


def area_plot():
    plt.figure(figsize=(10,6))

    days = [1,2,3,4,5]
    age =[63, 81, 52, 22, 37]
    weight =[17, 28, 72, 52, 32]
    plt.plot([],[], color='c', label = 'Weather Predicted', linewidth=5)
    plt.plot([],[],color = 'g', label='Weather Change happened', linewidth=5)
    plt.stackplot(days, age, weight, colors = ['c', 'g'])
    plt.xlabel('Fluctuation with time')
    plt.ylabel('Days')
    plt.title('Weather report using Area Plot')
    plt.legend()

    plt.savefig("output2.png", bbox_inches='tight')


def hist_plot():
    plt.figure(figsize=(10,6))

    pop = [22,55,62,45,21,22,34,42,42,4,2,8]
    bins = [1,10,20,30,40,50]
    plt.hist(pop, bins, rwidth=0.6)
    plt.xlabel('age groups')
    plt.ylabel('Number of people')
    plt.title('Histogram')
    
    plt.savefig("output2.png", bbox_inches='tight')

