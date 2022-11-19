# Electric Vehicle Parking System

---

### Synopsis

The purpose of this program was to design a parking reservation system for the University of the Fraser Valley.
This system is intended to allow students and staff members to reserve time blocks for charging their electric vehicles. Ultimately aiming at reducing parking-lot congestion and increasing efficiency of the end users.

---

### Build
``` bash
pyinstaller --clean evp.exe.spec
```
The .spec file I have provided should already contain all the information you need in order to build this binary as it should run. 
<br> If you should run into any issues here is the long command.

``` bash
pyinstaller --noconfirm --onefile --windowed --clean -n evp.exe main.py --add-data "images;images" --add-data "README.md;." --add-data "reservations.db;." --icon "images/ufv.png"
```

---

### Install / Run
This program currently does not require any cmd line arguments, environment_variables or other relative input. Simply execute the binary and follow the linear progression.
The binary after pyinstaller creation, will be located in the /dist/ directory.
``` bash
./dist/evp.exe
```

---


### Credits:

Project Lead: Frank Zhang<br>
Development Lead: Brian Atkinson <br>
