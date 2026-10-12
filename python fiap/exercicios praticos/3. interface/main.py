import customtkinter as ctk

#Configuraçao aparecencia
ctk.set_appearance_mode('dark')

#Criacao das funcoes de funcionalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == 'jonathan' and senha == '12345':
        resultado_login.configure(text='Login realizado',text_color='green')
    else:
        resultado_login.configure(text='Login incorreto',text_color='red')
#Criacao da janela principal
app = ctk.CTk()
app.title('Sistema de login')
app.geometry('300x300')


#Criacao dos campos

##Label
label_usuario = ctk.CTkLabel(app,text='Usuario:')
label_usuario.pack(pady=10)
##Entry
campo_usuario = ctk.CTkEntry(app,placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)

##Label
label_senha = ctk.CTkLabel(app,text='Senha:')
label_senha.pack(pady=10)
##Entry
campo_senha = ctk.CTkEntry(app,placeholder_text='Digite sua senha:',show='*')
campo_senha.pack(pady=10)

##Button
botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=10)

#campo feedback de login
resultado_login = ctk.CTkLabel(app,text='')
resultado_login.pack(pady=10)



#Iniciar a aplicacao
app.mainloop()
