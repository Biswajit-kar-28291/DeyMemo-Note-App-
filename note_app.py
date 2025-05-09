from flask import Flask, render_template, request, redirect,url_for
import os
import random

app = Flask(__name__)
color_pairs = {
    "Ocean Breeze": {
        "background": "#1abc9c",  # Soft turquoise
        "text": "#ffffff"  # White text
    },
    "Midnight Sky": {
        "background": "#2c3e50",  # Deep blue-gray
        "text": "#ecf0f1"  # Light silver
    },
    "Sunset": {
        "background": "#f39c12",  # Golden yellow
        "text": "#2c3e50"  # Dark blue-gray
    },
    "Cool Night": {
        "background": "#34495e",  # Charcoal blue
        "text": "#ecf0f1"  # Soft white
    },
    "Tropical Dream": {
        "background": "#e74c3c",  # Bright coral red
        "text": "#ecf0f1"  # Light silver
    },
    "Forest Grove": {
        "background": "#27ae60",  # Green
        "text": "#ffffff"  # White
    },
    "Lavender Bliss": {
        "background": "#9b59b6",  # Lavender purple
        "text": "#ffffff"  # White
    },
    "Pastel Breeze": {
        "background": "#f1c40f",  # Pastel yellow
        "text": "#2c3e50"  # Dark blue-gray
    },
    "Peachy Delight": {
        "background": "#e67e22",  # Peach orange
        "text": "#ffffff"  # White
    },
    "Classic Elegance": {
        "background": "#95a5a6",  # Grey
        "text": "#2c3e50"  # Dark blue-gray
    },
    "Soft Rose": {
        "background": "#f8c9c0",  # Soft rose pink
        "text": "#2c3e50"  # Dark blue-gray
    }
}

color_pairs2 = {
    "Neo Mint": {"background": "#ADEFD1", "text": "#00203F"},
    "Royal Purple": {"background": "#6A0DAD", "text": "#FFFFFF"},
    "Sunset Orange": {"background": "#FF5733", "text": "#FFFFFF"},
    "Deep Teal": {"background": "#004D40", "text": "#E0F2F1"},
    "Electric Blue": {"background": "#0074D9", "text": "#FFFFFF"},
    "Pastel Peach": {"background": "#FFDAB9", "text": "#5D3A00"},
    "Blush Pink": {"background": "#FFC0CB", "text": "#2C2C2C"},
    "Slate Gray": {"background": "#2F4F4F", "text": "#F5F5F5"},
    "Golden Yellow": {"background": "#FFDD57", "text": "#3E3E3E"},
    "Coral Red": {"background": "#E63946", "text": "#F1FAEE"},
    "Sky Blue": {"background": "#87CEEB", "text": "#1B1B1B"},
    "Midnight Blue": {"background": "#191970", "text": "#FFFFFF"}
}



@app.route("/", methods=['GET','POST'])
def reg():
    if request.method=="GET":
        return render_template("reg.html")
    elif request.method=="POST":
        n_name=request.form.get("n_username")
        n_name=n_name.replace(" ",'')
        n_pass=request.form.get("n_pass")
        n_pass=n_pass.replace(" ", '')
        r=[]
        f=open("login.txt","r")
        read=f.readlines()
        for i in read:
            a=i.split(",")
            r.append(a[0])
        if n_name in r:
            return render_template("reg.html", msg="please login !!" )
        else:

            f=open("login.txt","a")
            
            f.write(f'{n_name},{n_pass}\n')
            f.close()
            f=open("login.txt","r")
            l=[]
            s=f.readline()
            l.append(s)
            while (s!=""):
                s=f.readline()
                # a=s.split(",")
                l.append(a)
            f.close()


            return render_template("reg.html",msg="sussefully registard")

# def login():
#      flag=False
#      if request.method=="GET":
#           return render_template('login.html')
#      elif request.method=="POST":
#          name=request.form.get("username")
#          p=request.form.get("pass")
#          f=open("login.txt","r")
#          read=f.readlines()
         
#          for i in read:
#              na=i.split(",")
#         #  return render_template("reg.html", msg = (a[1][:-1]=="123"))
#             # na=i.split(",")
#              if name==na[0] and p==na[1][:-1]:
#                 flag=True
#          if flag:
#              if not os.path.exists(f'{name}.txt'):
#                  with open(f'{name}.txt', 'w') as f:
#                     f.write(f' hello{name}.\n')
#              return redirect(f'/{name}')
#          else:
#              return render_template("login.html", msg="you are not registerd !!")

     

@app.route("/login",methods=['GET','POST'] )
def login():
     flag=False
     if request.method=="GET":
          return render_template('login.html')
     elif request.method=="POST":
         name=request.form.get("username")
         p=request.form.get("pass")
         f=open("login.txt","r")
         read=f.readlines()
         
         for i in read:
             na=i.split(",")
        #  return render_template("reg.html", msg = (a[1][:-1]=="123"))
            # na=i.split(",")
             if name==na[0] and p==na[1][:-1]:
                flag=True
         if flag:
             if not os.path.exists(f'{name}.txt'):
                 with open(f'{name}.txt', 'w') as f:
                    f.write(f' hello{name}.\n')
             return redirect(f'/{name}')
         else:
             return render_template("login.html", msg="you are not registerd !!")
# def reg():
#     if request.method=="GET":
#         return render_template("reg.html")
#     elif request.method=="POST":
#         n_name=request.form.get("n_username")
#         n_name=n_name.replace(" ",'')
#         n_pass=request.form.get("n_pass")
#         n_pass=n_pass.replace(" ", '')
#         r=[]
#         f=open("login.txt","r")
#         read=f.readlines()
#         for i in read:
#             a=i.split(",")
#             r.append(a[0])
#         if n_name in r:
#             return render_template("reg.html", msg="you are registard")
#         else:

#             f=open("login.txt","a")
            
#             f.write(f'{n_name},{n_pass}\n')
#             f.close()
#             f=open("login.txt","r")
#             l=[]
#             s=f.readline()
#             l.append(s)
#             while (s!=""):
#                 s=f.readline()
#                 # a=s.split(",")
#                 l.append(a)
#             f.close()


#             return render_template("reg.html",msg="sussefully registard")


    

@app.route('/<name>')
def index(name):
    
        l=[]
        
        f=open(f'{name}.txt',"r")
        i=0
        
        s=f.readline()
        # l.append(f'{s[:len(s)]}{i}')    
        while(s!=""):
            i+=1
            s=f.readline()
            l.append(f'{s[:len(s)]}{i}')
            
        f.close()
        L= sorted(l, key=lambda person: person[-1], reverse=True)
        picked = random.choice(list(color_pairs.keys()))
        picked1 = random.choice(list(color_pairs2.keys()))

        return render_template('note_app.html',big_box_bc=color_pairs2[picked1]["background"],big_box_c=color_pairs2[picked1]["text"], notes=L,nam=name, bc=color_pairs[picked]["background"], c=color_pairs[picked]["text"])

@app.route('/<name>/add', methods=['POST'])
def add_note(name):
    f=open(f'{name}.txt',"a")
    note = request.form.get('note')
    if note:
        f.write(f'{note}\n')
    f.close()
    return redirect(f'/{name}')

@app.route('/<name>/delete/<int:index>')
def delete_note(name,index):
    if 1 <= index :
    
        f=open(f'{name}.txt',"r")
        lines=f.readlines()
        del lines[int(index)]
        f=open(f'{name}.txt',"w")
        f.writelines(lines)
        return redirect(f'/{name}')
    

if __name__ == '__main__':
    app.run( host="192.168.29.47",debug=True)
