# :card_file_box: VeloData
A tool for transfering **+256TB** **encrypted** files for free. Currently restricted to transfers on the same local network.

## :hammer: Technologies
* ```pycryptodome```
* ```PySide6```
* ```Python```
* ```Multithreading```
* ```TCP```

## :rocket: Features
* Client for sending data
* Server for recieving data

## :bookmark: The Process
Started off by getting acquainted with the PySide6 designer tool, since it was my very first time using it. I designed a simple and minimalistic design for the app and shortly afterwards started programming. I hooked up the buttons and decided that the transferred that should be encrypted. 

I had some challenges with the QT framework. The implementation of different threads for sending data and receiving data were a bit tricky. I quickly learned that signals existed which let me safely communicate between threads and the UI. I also implemented a custom label with a drag and drop event that can receive files. 

AES encryption was also a part that I wanted to implement. It was interesting to learn more about encryption since it was my first project where I implemented it.

I used TCP connection to transfer data between machines. I created different headers with the filename and file size, which is read by the receiver, so it knows how big different files are. 

Overall it was a interesting project where I learned much about TCP, data encryption, transferring data, designing the application and the QT framework!

## :rotating_light: Requirements
Make sure to have the following python modules installed for the server to work correctly:
* PySide6
* pycryptodome

## :vertical_traffic_light: Setting up DB and running API
1. Clone the repository to your local machine.
2. Setup the key and noise in the ```Data/Scripts/socket_logic.py```. Keep in mind that they both have to be a string of 16 char.
3. Run ```main.py```.



