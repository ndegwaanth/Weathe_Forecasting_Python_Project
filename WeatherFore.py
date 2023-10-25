import tkinter
from tkinter import messagebox
import webbrowser

# from tkinter import ttk

window = tkinter.Tk()
window.title('Weather')
window.resizable(True, True)
window.geometry('800x800')

get = tkinter.StringVar()


# def submitact():
#     Phone_number1 = Phone_numberEntry.get()
#     Name = nameEntry.get()
#     Email1 = EmailEntry.get()
#     Password1 = PasswordEntry.get()
#     comfirm_password1 = comfirm_passwordEntry.get()
#     login_into_db(Phone_number1, Name, Password1, Email1, comfirm_password1)


# def login_into_db(Phone_number1, Name, Password1, Email1, comfirm_password1):
#     global conn, cursor
#     if Phone_number1:
#         if Name and Password1 and Email1 and comfirm_password1:
#             conn = pyodbc.connect('Driver = {SQL Server};'
#                                   'sever = DESKTOP-2HTJ4SJ\SQLEXPRESS02;'
#                                   'Database = Farmers_Details ;'
#                                   'Trusted_connection = yes')

#             cursor = conn.cursor()
#     else:
#         conn = pyodbc.connect('Driver = {SQL Server};'
#                               'sever = DESKTOP-2HTJ4SJ\SQLEXPRESS02 ;'
#                               'Database = Farmers_Details ;'
#                               'Trusted_connection = yes')
#         cursor = conn.cursor()

#     save = "select * from Details"

#     try:
#         cursor.execute(save)
#         result = cursor.fetchall()
#         for x in result:
#             print(x)
#         print("Querry executed Sucessfully")
#     except:
#         conn.rollback()
#         print("Error Occurred")


# The image in the window background
# image1 = Image.open('pexel.jpg')
# label = ImageTk.PhotoImage(image1)
# lbl = tkinter.Label(window, image=label, height=800, width=800, padx=0, pady=0)
# lbl.place(x=0, y=0)


# this are the placeholders in the page 1 Entry boxes
def click0(*args):
    nameEntry.delete(0, 'end')


def click1(*args):
    EmailEntry.delete(0, tkinter.END)


def click2(*args):
    Phone_numberEntry.delete(0, tkinter.END)


def click3(*args):
    comfirm_passwordEntry.delete(0, tkinter.END)


def click4(*args):
    PasswordEntry.delete(0, tkinter.END)


# def click5(*args):
#   LocationEntry.delete(0, tkinter.END)

def leave0(*args):
    nameEntry.delete(0, 'end')
    nameEntry.insert(0, 'Enter Full Names')
    # nameEntry.focus_force()
    window.focus()


def leave1(*args):
    EmailEntry.delete(0, 'end')
    EmailEntry.insert(0, 'Enter Email')
    EmailEntry.get()
    window.focus()


def leave2(*args):
    Phone_numberEntry.delete(0, 'end')
    Phone_numberEntry.insert(0, 'Enter phone_number')
    window.focus()


def leave3(*args):
    comfirm_passwordEntry.delete(0, 'end')
    comfirm_passwordEntry.insert(0, 'Comfirm Password')
    window.focus()


def leave4(*args):
    PasswordEntry.delete(0, 'end')
    PasswordEntry.insert(0, 'Enter the password')
    window.focus()

    # def leave5(*args):
    #   LocationEntry.delete(0, tkinter.END)
    #   LocationEntry.insert(0, 'Enter the location')
    #   window.focus()

    window.focus()


def Nonextstage():
    if error_detection() == None:
        messagebox.showinfo('Details', 'Submission Failed')
    elif error_detection() == '':
        messagebox.showinfo('Details', 'Submission Successful')


# fullname = string
# location = string
# phone_number = string
# password = string
# comfirm_p = string
# email1 = string
# OM = string
# OM.set('select location')

def view():
    PasswordEntry.configure(show='*')
    PasswordEntry.configure(command=hide1)


def view1():
    comfirm_passwordEntry.configure(show='*')
    comfirm_passwordEntry.configure(command=hide2)


def hide1():
    PasswordEntry.configure(show='*')
    PasswordEntry.columnconfigure(command=view)


def hide2():
    comfirm_passwordEntry.configure(show='*')
    comfirm_passwordEntry.configure(command=hide2)


def Details():
    # from PIL import Image, ImageTk
    import webbrowser
    # import codecs
    from tkinter import ttk

    myWindow = tkinter.Tk()
    myWindow.title('Riftvalley Regions')
    myWindow.configure(background='blue')
    myWindow.geometry('800x800')
    myWindow.resizable(True, True)

    # image2 = Image.open('LION.jpg')
    # Icon1 = ImageTk.PhotoImage(image2)
    # identity = tkinter.Label(myWindow, image=Icon1, height=800, width=800, padx=0, pady=0)
    # identity.place(x=0, y=0)
    # print('This is a new window')

    data = tkinter.Label(myWindow, text='WELCOME TO RIFTVALLEY REGION', font='arial, 15')
    data.grid(row=0, column=0, pady=50, padx=50)
    data1 = tkinter.Label(myWindow,
                          text='Nature is painting for us, day after day, pictures of infinite beauty\n if only we have the eyes to see them',
                          font='arial, 16', bg='blue')
    data1.grid(row=60, column=0)
    frame1 = tkinter.Frame(myWindow, width=400, height=400, bg='grey')
    frame1.grid(row=70, column=0, sticky=tkinter.NW, pady=50, padx=50)
    label6 = tkinter.Label(frame1, text='Choose the County you belong', font='Helvetica, 14', bd=2)
    label6.grid(row=70, column=20, padx=50, pady=50)

    def show():
        myLabel = tkinter.Label(frame1, text=enter.get())
        myLabel.grid(row=200, column=20, pady=10, padx=10)

    # This consist of are the subcounties in the riftvalley region
    subcounties1 = ["Baringo Central", "Baringo North", "Baringo South", "Eldama Ravine", "Mogotio", "Tiaty",
                    "Bomet Central", "Bomet East", "Bomet West", "Chepalungu", "Konoin", "Sotik", "Keiyo North",
                    "Keiyo South", "Marakwet East", "Marakwet West", "Ainamoi", "Belgut", "Bureti", "Kipkelion East",
                    "Kipkelion West", "Soin/Sigowet", "Laikipia Central", "Laikipia East", "Laikipia North",
                    "Laikipia West", "Gilgil", "Kuresoi North", "Kuresoi South", "Molo", "Naivasha", "Nakuru East",
                    "Nakuru North",
                    "Nakuru West", "Njoro", "Rongai", "Aldai", "Chesumei", "Emgwen", "Mosop", "Nandi East",
                    "Nandi Hills",
                    "Tinderet", "Narok East", "Narok North", "Narok South", "Narok West", "Transmara East",
                    "Transmara West", "Samburu East", "Samburu North", "Samburu West", "Cherangany", "Endebess",
                    "Kiminini", "Saboti",
                    "Ainabkoi", "Kapseret", "Kesses", "Moiben", "Soy", "Turbo"]

    enter = tkinter.StringVar(myWindow)
    enter.set(subcounties1[0])
    press = tkinter.OptionMenu(frame1, enter, *subcounties1)
    press.grid(row=160, column=20)
    press.config(width=20)
    mybutton = tkinter.Button(frame1, text='show selection', command=lambda: [show()])
    mybutton.grid(row=250, column=20)

    # def Elgeyo_marakwet():
    #     if get.get() == 'google2':
    #         f = open('web.html', 'w')
    #         template = """"
    #                <!DOCTYPE html>
    #                <html lang="en">
    #                <head>
    #                    <meta charset="UTF-8">
    #                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    #                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #                    <title>Baringo_county</title>
    #                </head>
    #                <body>
    #                    <h1>Baringo County is located in Kenya and has two main rainy seasons: the long rains from March to June and the short rains from October to December. The county also experiences a dry season from January to March and a hot season from July to September. Based on
    #                         these weather seasons, here are some crops that can be planted in Baringo County:</h1>
    #                     <ol>
    #                        <li>
    #                        Long Rains (March to June):
    #
    #                            <ul>
    #                                <li>Maize: This is a staple crop in Kenya and can be planted during the long rains.
    #                                    Maize requires a lot of water and fertile soil to grow well.</li>
    #                                <li>Beans: Beans are legumes and can be grown alongside maize.
    #                                    They fix nitrogen in the soil, making it more fertile for other crops.</li>
    #                                <li>Sorghum: Sorghum is drought-tolerant and can withstand the long dry spells that may occur during the rainy season.
    #                                    It can be planted alongside maize and beans.</li>
    #                            </ul>
    #
    #                        </li>
    #                        <h3>During this season, crops that can withstand the occasional drought and are fast-maturing can be planted.
    #                             Some of the crops that can be planted during the short rains in Baringo County include:</h3>
    #                        <li>Short Rains (October to December):</li>
    #                         <ul>
    #                            <li>Green Grams: These are fast-maturing and can be harvested within two to three months.
    #                                They are also drought-tolerant and can withstand the occasional dry spell.</li>
    #                            <li>Green Grams: These are fast-maturing and can be harvested within two to three months.
    #                                 They are also drought-tolerant and can withstand the occasional dry spell.</li>
    #                            <li>Cowpeas: Cowpeas are also fast-maturing and can be harvested within two to three months.
    #                                 They are also drought-tolerant and can be grown in combination with green grams.</li>
    #                            <li>Amaranth: Amaranth is a leafy vegetable that can be grown during the short rains.
    #                                It is rich in nutrients and can be a source of food and income for farmers.</li>
    #                         </ul>
    #                     </ol>
    #                    <ol class="DryJam1">Dry Season (January to March):</ol>
    #                     <h5>During this season, crops that can grow well in dry conditions can be planted.
    #                         Some of the crops that can be planted during the dry season in Baringo County include:</h5>
    #                         <ul>
    #                            <li>Tomatoes: Tomatoes can be grown in greenhouses during the dry season.
    #                                 They require regular watering and fertilization to grow well.</li>
    #                            <li>Capsicum: Capsicum is a pepper that can also be grown in greenhouses during the dry season.
    #                                It requires regular watering and fertilization to grow well.</li>
    #                            <li>Kales: Kales are leafy vegetables that can be grown in kitchen gardens during the dry season.
    #                                 They are easy to grow and require little water.</li>
    #                         </ul>
    #                    <ol class="JUS1">Hot Season (July to September):</ol>
    #                    <h5>During this season, crops that can withstand the hot temperatures can be planted.
    #                         Some of the crops that can be planted during the hot season in Baringo County include:</h5>
    #                         <ul>
    #                            <li>Watermelon: Watermelon is a fruit that requires a lot of water to grow well.
    #                                 It can be planted during the hot season as it can withstand the hot temperatures.</li>
    #                            <li>Pumpkin: Pumpkin is a vegetable that can also be planted during the hot season.
    #                                 It requires regular watering to grow well.</li>
    #                            <li>Sweet potato: Sweet potato is a root crop that can be planted during the hot season.
    #                                It requires little water to grow and can withstand the hot temperatures.</li>
    #                         </ul>
    #                </body>
    #                </html>
    #
    #                """
    #         f.write(template)
    #
    #         # codecs open the file that is utf-8 rather than ASCI
    #         file = codecs.open('web.html', 'r', "utf-8")
    #
    #         # now i display what is contained in the template on the console
    #         print(file.read())
    #
    #         # using the module of the webbrowser i can access the content on the creates web page
    #         webbrowser.open('web.html')
    #         f.close()

    # def Baringo():

    #     if get.get() == 'google':
    #         f = open('web.html', 'w')
    #         template = """"
    #         <!DOCTYPE html>
    #         <html lang="en">
    #         <head>
    #             <meta charset="UTF-8">
    #             <meta http-equiv="X-UA-Compatible" content="IE=edge">
    #             <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #             <title>Baringo_county</title>
    #         </head>
    #         <style>
    #             .DryJam1 {
    #                 color:blue;
    #                 background-color: aqua;
    #                 border: none;
    #                 height: 36px;
    #                 width: 120px;
    #                 border-radius: 20px;
    #                 cursor: pointer;
    #                 padding-bottom: 20px;
    #             }
    #
    #             .JUS1 {
    #                 color:blue;
    #                 background-color: aqua;
    #                 border: none;
    #                 height: 36px;
    #                 width: 120px;
    #                 border-radius: 20px;
    #                 cursor: pointer;
    #                 padding-bottom: 20px;
    #             }
    #
    #         </style>
    #         <body>
    #             <h1>Baringo County is located in Kenya and has two main rainy seasons: the long rains from March to June and the short rains from October to December. The county also experiences a dry season from January to March and a hot season from July to September. Based on
    #                  these weather seasons, here are some crops that can be planted in Baringo County:</h1>
    #              <ol>
    #                 <li>
    #                 Long Rains (March to June):
    #
    #                     <ul>
    #                         <li>Maize: This is a staple crop in Kenya and can be planted during the long rains.
    #                             Maize requires a lot of water and fertile soil to grow well.</li>
    #                         <li>Beans: Beans are legumes and can be grown alongside maize.
    #                             They fix nitrogen in the soil, making it more fertile for other crops.</li>
    #                         <li>Sorghum: Sorghum is drought-tolerant and can withstand the long dry spells that may occur during the rainy season.
    #                             It can be planted alongside maize and beans.</li>
    #                     </ul>
    #
    #                 </li>
    #                 <h3>During this season, crops that can withstand the occasional drought and are fast-maturing can be planted.
    #                      Some of the crops that can be planted during the short rains in Baringo County include:</h3>
    #                 <li>Short Rains (October to December):</li>
    #                  <ul>
    #                     <li>Green Grams: These are fast-maturing and can be harvested within two to three months.
    #                         They are also drought-tolerant and can withstand the occasional dry spell.</li>
    #                     <li>Green Grams: These are fast-maturing and can be harvested within two to three months.
    #                          They are also drought-tolerant and can withstand the occasional dry spell.</li>
    #                     <li>Cowpeas: Cowpeas are also fast-maturing and can be harvested within two to three months.
    #                          They are also drought-tolerant and can be grown in combination with green grams.</li>
    #                     <li>Amaranth: Amaranth is a leafy vegetable that can be grown during the short rains.
    #                         It is rich in nutrients and can be a source of food and income for farmers.</li>
    #                  </ul>
    #              </ol>
    #             <ol class="DryJam1">Dry Season (January to March):</ol>
    #              <h5>During this season, crops that can grow well in dry conditions can be planted.
    #                  Some of the crops that can be planted during the dry season in Baringo County include:</h5>
    #                  <ul>
    #                     <li>Tomatoes: Tomatoes can be grown in greenhouses during the dry season.
    #                          They require regular watering and fertilization to grow well.</li>
    #                     <li>Capsicum: Capsicum is a pepper that can also be grown in greenhouses during the dry season.
    #                         It requires regular watering and fertilization to grow well.</li>
    #                     <li>Kales: Kales are leafy vegetables that can be grown in kitchen gardens during the dry season.
    #                          They are easy to grow and require little water.</li>
    #                  </ul>
    #             <ol class="JUS1">Hot Season (July to September):</ol>
    #             <h5>During this season, crops that can withstand the hot temperatures can be planted.
    #                  Some of the crops that can be planted during the hot season in Baringo County include:</h5>
    #                  <ul>
    #                     <li>Watermelon: Watermelon is a fruit that requires a lot of water to grow well.
    #                          It can be planted during the hot season as it can withstand the hot temperatures.</li>
    #                     <li>Pumpkin: Pumpkin is a vegetable that can also be planted during the hot season.
    #                          It requires regular watering to grow well.</li>
    #                     <li>Sweet potato: Sweet potato is a root crop that can be planted during the hot season.
    #                         It requires little water to grow and can withstand the hot temperatures.</li>
    #                  </ul>
    #         </body>
    #         </html>
    #
    #         """
    #         f.write(template)
    #
    #
    #         # codecs open the file that is utf-8 rather than ASCI
    #         file = codecs.open('web.html', 'r', "utf-8")
    #
    #         # now i display what is contained in the template on the console
    #         print(file.read())
    #
    #         # using the module of the webbrowser i can access the content on the creates web page
    #         webbrowser.open('web.html')
    #         f.close()

    def Baringo():
        webbrowser.open('http://127.0.0.1:5555/sub1.html')

    # def Bomet():
    #         f1 = open('web1.html', 'w')
    #
    #         template = """"
    #            <!DOCTYPE html>
    #     <html lang="en">
    #     <head>
    #     <meta charset="UTF-8">
    #     <meta http-equiv="X-UA-Compatible" content="IE=edge">
    #     <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #     <title>Baringo_county</title>
    #     </head>
    #     <style>
    #     .DryJam {
    #         color:blue;
    #         background-color: aqua;
    #         border: none;
    #         height: 36px;
    #         width: 120px;
    #         border-radius: 20px;
    #         cursor: pointer;
    #         padding-bottom: 20px;
    #     }
    #
    #     .JUS {
    #         color:blue;
    #         background-color: aqua;
    #         border: none;
    #         height: 36px;
    #         width: 120px;
    #         border-radius: 20px;
    #         cursor: pointer;
    #         padding-bottom: 20px;
    #     }
    #
    # </style>
    # <body>
    #     <h1>Bomet County is located in Kenya and has two main rainy seasons: the long rains from March to May and the short rains from October to December. The county also experiences a dry season from January to March and a hot season from June to September.
    #         Based on these weather seasons, here are some crops that can be planted in Bomet County::</h1>
    #      <ol>
    #         <li>
    #         Long Rains (March to May):
    #         <h5>During this season, crops that require a lot of water can be planted.
    #              Some of the crops that can be planted during the long rains in Bomet County include:</h5>
    #
    #             <ul>
    #                 <li>Maize: This is a staple crop in Kenya and can be planted during the long rains.
    #                      Maize requires a lot of water and fertile soil to grow well.</li>
    #                 <li>Beans: Beans are legumes and can be grown alongside maize.
    #                      They fix nitrogen in the soil, making it more fertile for other crops.</li>
    #                 <li>Irish potatoes: Irish potatoes can be grown during the long rains.
    #                      They require well-drained soil and regular watering.<li>
    #              </ul>
    #
    #         <li>Short Rains (October to December):</li>
    #           <h5>During this season, crops that can withstand the occasional drought and are fast-maturing can be planted.
    #             Some of the crops that can be planted during the short rains in Bomet County include:</h5>
    #          <ul>
    #             <li>Green Grams: These are fast-maturing and can be harvested within two to three months.
    #                 They are also drought-tolerant and can withstand the occasional dry spell.</li>
    #             <li>Cowpeas: Cowpeas are also fast-maturing and can be harvested within two to three months.
    #                  They are also drought-tolerant and can be grown in combination with green grams.</li>
    #             <li>Amaranth: Amaranth is a leafy vegetable that can be grown during the short rains.
    #                 It is rich in nutrients and can be a source of food and income for farmers.</li>
    #          </ul>
    #      </ol>
    #     <ol class="DryJam">Dry Season (January to March):</ol>
    #      <h5>During this season, crops that can grow well in dry conditions can be planted.
    #          Some of the crops that can be planted during the dry season in Bomet County include:</h5>
    #          <ul>
    #             <li>Tomatoes: Tomatoes can be grown in greenhouses during the dry season.
    #                  They require regular watering and fertilization to grow well.</li>
    #             <li>Capsicum: Capsicum is a pepper that can also be grown in greenhouses during the dry season.
    #                 It requires regular watering and fertilization to grow well.</li>
    #             <li>Kales: Kales are leafy vegetables that can be grown in kitchen gardens during the dry season.
    #                  They are easy to grow and require little water.</li>
    #          </ul>
    #     <ol class="JUS">Hot Season (June to September):</ol>
    #     <h5>During this season, crops that can withstand the hot temperatures can be planted.
    #          Some of the crops that can be planted during the hot season in Baringo County include:</h5>
    #          <ul>
    #             <li>Watermelon: Watermelon is a fruit that requires a lot of water to grow well.
    #                  It can be planted during the hot season as it can withstand the hot temperatures.</li>
    #             <li>Pumpkin: Pumpkin is a vegetable that can also be planted during the hot season.
    #                  It requires regular watering to grow well.</li>
    #             <li>Sweet potato: Sweet potato is a root crop that can be planted during the hot season.
    #                 It requires little water to grow and can withstand the hot temperatures.</li>
    #          </ul>
    # </body>
    # </html>
    #         """
    #         f1.write(template)
    #         f1.close()
    #
    #         # codecs open the file that is utf-8 rather than ASCI
    #         file1 = codecs.open('web1.html', 'r', "utf-8")
    #
    #         # now i display what is contained in the template on the console
    #         print(file1.read())
    #
    #         # using the module of the webbrowser i can access the content on the creates web page
    #         webbrowser.open('web1.html')
    def CountySearch():
        if get.get() == 'google1':
            webbrowser.open('http://127.0.0.1:5555/Bomet.html')
        if get.get() == 'web':
            webbrowser.open('http://127.0.0.1:5555/Baringo.html')
        if get.get() == 'google11':
            webbrowser.open('http://127.0.0.1:5555/Turkana.html')
        if get.get() == 'google7':
            webbrowser.open('http://127.0.0.1:5555/Nandi.html')
        if get.get() == 'google2':
            webbrowser.open('http://127.0.0.1:5555/Elgeyo_marakwet.html')
        if get.get() == 'google3':
            webbrowser.open('http://127.0.0.1:5555/Kajiando.html')
        if get.get() == 'google4':
            webbrowser.open('http://127.0.0.1:5555/Kericho.html')
        if get.get() == 'google5':
            webbrowser.open('http://127.0.0.1:5555/Laikipia.html')
        if get.get() == 'google5':
            webbrowser.open('http://127.0.0.1:5555/Laikipia.html')
        if get.get() == 'google6':
            webbrowser.open('http://127.0.0.1:5555/Nakuru.html')
        if get.get() == 'google8':
            webbrowser.open('http://127.0.0.1:5555/Narok.html')
        if get.get() == 'google9':
            webbrowser.open('http://127.0.0.1:5555/Samburu.html')
        if get.get() == 'google10':
            webbrowser.open('http://127.0.0.1:5555/Trans_Nzoia.html')
        if get.get() == 'google12':
            webbrowser.open('http://127.0.0.1:5555/Uasin_Gishu.html')



    frame2 = tkinter.Frame(myWindow, width=400, height=400)
    frame2.place(x=400, y=232)

    query = tkinter.Label(frame2, text='Querry', bd=4, font=('arial', 14, 'bold'))
    query.place(x=0, y=0)

    questionField = tkinter.Entry(frame2, width=20, font=('arial', 14, 'bold'), bd=4)
    questionField.place(x=90, y=0)

    labelv = tkinter.Label(frame2, text='Select your County Below', bd='2', bg='Blue', width=20, height=0, padx=10)
    labelv.place(x=5, y=50)

    # mic1 = Image.open('mic2.png')
    # micImage1 = ImageTk.PhotoImage(mic1)
    # micButton1 = tkinter.Button(frame2, image=micImage1, bg='lightgrey', bd=0, cursor='hand2',
    #                             activebackground='lightgrey', width=10, height=25)
    # micButton1.place(x=100, y=0)

    # search = Image.open('search1.png')
    # searchImage = ImageTk.PhotoImage(search)
    # searchButton = tkinter.Button(frame2, image=searchImage, bg='lightweight', bd=0, cursor='hand2',
    #                               activebackground='lightweight', command=CountySearch)
    # searchButton.grid(row=0, column=3, padx=5)

    style = ttk.Style()
    print(style.theme_names())
    style.theme_use('vista')
    radiobutton1 = ttk.Radiobutton(frame2, text='Baringo', value='web', variable=get)
    radiobutton1.place(x=0, y=80)
    radiobutton2 = ttk.Radiobutton(frame2, text='Bomet', value='google1', variable=get)
    radiobutton2.place(x=0, y=100)
    radiobutton3 = ttk.Radiobutton(frame2, text='Elgeyo_marakwet', value='google2', variable=get)
    radiobutton3.place(x=0, y=120)
    radiobutton4 = ttk.Radiobutton(frame2, text='Kajiando', value='google3', variable=get)
    radiobutton4.place(x=0, y=140)
    radiobutton5 = ttk.Radiobutton(frame2, text='Kericho', value='google4', variable=get)
    radiobutton5.place(x=0, y=160)
    radiobutton6 = ttk.Radiobutton(frame2, text='Laikipia', value='google5', variable=get)
    radiobutton6.place(x=0, y=180)
    radiobutton7 = ttk.Radiobutton(frame2, text='Nakuru', value='google6', variable=get)
    radiobutton7.place(x=0, y=200)
    radiobutton8 = ttk.Radiobutton(frame2, text='Nandi', value='google7', variable=get)
    radiobutton8.place(x=0, y=220)
    radiobutton9 = ttk.Radiobutton(frame2, text='Narok', value='google8', variable=get)
    radiobutton9.place(x=0, y=240)
    radiobutton10 = ttk.Radiobutton(frame2, text='Samburu', value='google9', variable=get)
    radiobutton10.place(x=0, y=260)
    radiobutton11 = ttk.Radiobutton(frame2, text='Trans_Nzoia', value='google10', variable=get)
    radiobutton11.place(x=0, y=280)
    radiobutton12 = ttk.Radiobutton(frame2, text='Turkana', value='google11', variable=get)
    radiobutton12.place(x=0, y=300)
    radiobutton13 = ttk.Radiobutton(frame2, text='Uasin_Gishu', value='google12', variable=get)
    radiobutton13.place(x=0, y=320)


def NewWindow():
    import tkinter

    window1 = tkinter.Tk()
    window1.title('login Page')
    window1.resizable(True, True)
    window1.config(background='grey')
    window1.geometry('800x800')

    # image = Image.open('images.jpeg')
    # Icon = ImageTk.PhotoImage(image)
    # identity = tkinter.Label(window1, image=Icon, height=800, width=800, padx=0, pady=0)
    # identity.place(x=0, y=0)
    # print('This is a new window')

    # def Paragraph():
    #   doc = docx.Document()
    #   doc.add_heading('Welcom to RiftValley Region', 0)
    #   doc.add_paragraph(
    #     '''Nature is painting for us, day after day, pictures of infinite beauty if only we have the eyes to see them''')
    #   doc.save('gfg.docx')
    #   print("Nature is painting for us, day after day, pictures of infinite beauty if only we have the eyes to see them ")

    frame = tkinter.Frame(window1, width=200, height=150)
    frame.grid(row=20, column=10)

    lab5 = tkinter.Label(frame, text='Enter your Email', bd=2, width=15, font='arial, 14')
    lab5.grid(row=20, column=30)
    entry = tkinter.Entry(frame, width=40, bd=3)
    entry.grid(row=20, column=31, padx=10, pady=10)

    password1 = tkinter.Label(frame, text='Password', bd=2, width=15, font='arial, 14')
    password1.grid(row=40, column=30)
    entry1 = tkinter.Entry(frame, width=40, bd=3)
    entry1.grid(row=40, column=31, pady=10, padx=10)

    def callback(url):
        webbrowser.open_new_tab(url)

    link = tkinter.Label(frame, text='forgoten the password ?', font='Helveticabold, 10', fg='blue', cursor='hand2')
    link.grid(row=45, column=31, padx=10, pady=10)
    link.bind('button-1', lambda e: callback('forgotten your Password ?'))

    button3 = tkinter.Button(frame, text='Login in', font='arial, 12', bg='blue', width=27, command=Details)
    button3.grid(row=60, column=31, padx=10, pady=10)

    window1.mainloop()


# This is the new screen than pop up when the user click submit button
def openNewWindow():
    screen = tkinter.Tk()
    screen.title('WeatherForecasting')
    screen.geometry('800x800')
    screen.configure(background='blue')

    # image = Image.open('images.jpeg')
    # Icon = ImageTk.PhotoImage(image)
    # identity = tkinter.Label(window, image=Icon, height=800, width=800, padx=0, pady=0)
    # identity.place(x=0, y=0)
    # print('This is a new window')

    lab1 = tkinter.Label(screen, text='enter to search', pady=5, padx=20)
    lab1.grid(row=0, column=100)
    entry1 = tkinter.Entry(screen)
    entry1.config(font='ariall, 12', bd=2)
    entry1.grid(row=0, column=150)

    # implementing the search box
    button1 = tkinter.Button(screen, text='search', bd=3, bg='grey')
    button1.grid(row=2, column=150)
    button1.config(width=5)

    status = tkinter.Label(screen, text='...still waiting')
    status.grid(row=0, column=200)

    screen.mainloop()


# this function give the user an Error if he/she does not key in the details are of required implemented using the messagebox.showerror
def error_detection():
    if nameEntry.get() == '':
        messagebox.showerror('Error', 'enter your name')
    elif PasswordEntry.get() == '':
        messagebox.showerror('Érror', 'Enter the Password')
    elif comfirm_passwordEntry.get() == '':
        messagebox.showerror('Error', 'Enter the Password for comfirmation')
    elif Phone_numberEntry.get() == '':
        messagebox.showerror('Érror', 'Enter your Phone number')
    elif EmailEntry.get() == '':
        messagebox.showerror('Error', 'Enter your Email')


# This represent the label of the below entry boxes
name = tkinter.Label(window, text='Name   :', relief='raised', anchor='e', bd=2, font="arial, 14", bg='yellow')
name.grid(row=0, column=20)
nameEntry = tkinter.Entry(window)
nameEntry.config(bd=2, width=30)
nameEntry.grid(row=0, column=30, pady=15, padx=15)
Name = nameEntry.get()
nameEntry.insert(0, 'Enter Full Names ')
nameEntry.bind('<Button-1>', click0)
# nameEntry.bind('<Leave>', leave0)
nameEntry.focus_force()

# Phone_number label the entry of the Phone_number in the range of 0-9 and details are got from the user
Phone_number = tkinter.Label(window, text='Phone_number   :', relief='raised', anchor='e', bd=2, font="arial, 14",
                             bg='yellow')
Phone_number.grid(row=5, column=20)
Phone_numberEntry = tkinter.Entry(window)
Phone_numberEntry.grid(row=5, column=30, padx=15, pady=15)
Phone_numberEntry.config(width=30, bd=2)
Phone_number1 = Phone_numberEntry.get()
Phone_numberEntry.insert(0, 'enter phone number')
Phone_numberEntry.bind('<Button-1>', click2)
# Phone_numberEntry.bind('<Leave>', leave2)

# Email label the entry of the email and details are got from the user
Email = tkinter.Label(window, text='Email   :', relief='raised', anchor='e', bd=2, font="arial, 14", bg='yellow')
Email.grid(row=4, column=20)
EmailEntry = tkinter.Entry(window)
EmailEntry.grid(row=4, column=30, pady=15, padx=15)
EmailEntry.config(width=30, bd=2)
Email1 = EmailEntry.get()
EmailEntry.insert(0, 'Enter Email ')
EmailEntry.bind('<Button>', click1)
# EmailEntry.bind('<Leave>', leave1)

# password label, the entry box implemented and the password is got from the user
Password = tkinter.Label(window, text='Password   :', relief='raised', anchor='e', bd=2, font="arial, 14", bg='yellow')
Password.grid(row=6, column=20)
PasswordEntry = tkinter.Entry(window)
PasswordEntry.grid(row=6, column=30, pady=15, padx=15)
PasswordEntry.config(width=30, bd=2)
Password1 = PasswordEntry.get()
PasswordEntry.insert(0, 'Enter Password ')
PasswordEntry.bind('<Button-1>', click4)
# PasswordEntry.bind('<Leave>', leave4)

# check button to hide and unhide password
check1 = tkinter.Checkbutton(window, command=view)
check1.grid(row=6, column=34)

# The user key in the the password again to comfirm the previous password entered
comfirm_password = tkinter.Label(window, text='Comfirm_password   :', relief='raised', anchor='e', bd=2,
                                 font="arial, 14", bg='yellow')
comfirm_password.grid(row=8, column=20)
comfirm_passwordEntry = tkinter.Entry(window)
comfirm_passwordEntry.grid(row=8, column=30, pady=15, padx=15)
comfirm_passwordEntry.config(width=30, bd=2)
comfirm_password1 = comfirm_passwordEntry.get()
comfirm_passwordEntry.insert(0, 'comfirm Password')
comfirm_passwordEntry.bind('<Button-1>', click3)
# comfirm_passwordEntry.bind('<Leave>', leave3)

# the second chebutton for the hiding and viewing the password
check2 = tkinter.Checkbutton(window, command=view1)
check2.grid(row=8, column=34)

# nameEntry.delete(0, tkinter.END)
# EmailEntry.delete(0, tkinter.END)
# PasswordEntry.delete(0, tkinter.END)
# Phone_numberEntry.delete(0, tkinter.END)
# comfirm_passwordEntry.delete(0, tkinter.END)

# The submission button when the user enter the details
button = tkinter.Button(window, text='Sign Up', bg='yellow',
                        command=lambda: [error_detection(), Nonextstage(), Details(), ], pady=2,
                        padx=2)
# submitact()
button.config(width=10)
button.grid(row=40, column=30)

# button = tkinter.Button(window, text='Next', bg='yellow', command=openNewWindow, pady=2, padx=2)
# button.config(width=10)
# button.grid(row=40, column=80)

lab1 = tkinter.Label(window, text='have an account?', bd=1)
lab1.grid(row=80, column=30, padx=10, pady=10)

button2 = tkinter.Button(window, text='Login', bd=2, bg='blue', command=NewWindow)
button2.grid(row=80, column=40)
window.mainloop()
