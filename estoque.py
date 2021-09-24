from numpy.core.arrayprint import format_float_scientific
from numpy.core.fromnumeric import size
from numpy.core.numeric import True_
import pandas as pd
import tkinter as tk
from tkinter import *

df = pd.read_csv('estoque.csv', sep=';',encoding='cp1252',usecols=[1,2,7,9,11,14,55,56,57])

#informacoes adicionais
coleta  = df.loc[(df['SituacaoDescricao'] == 'Aguardando coleta')]
exp_pa  = df.loc[(df['SituacaoDescricao'] == 'Expedido para o PA')]
pre_saida  = df.loc[(df['SituacaoDescricao'] == 'Pré-Saída')]
new_gd  = df.loc[(df['SituacaoIndoorDescricao'] == 'NEW GOOD')]
gd  = df.loc[(df['SituacaoIndoorDescricao'] == 'GOOD')]
bd  = df.loc[(df['SituacaoIndoorDescricao'] == 'BAD')]
doa  = df.loc[(df['SituacaoIndoorDescricao'] == 'DOA')]
lib = df.loc[(df['SituacaoMovDescricao'] == 'Liberado')]
bloq = df.loc[(df['SituacaoMovDescricao'] == 'Bloqueado')]
res = df.loc[(df['SituacaoMovDescricao'] == 'Reservado')]



#EQUIPAMETNOS
aposa = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'APOSA8')]
a910s = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'A910S')]
d195 = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'D195')]
d195s = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'D195S')]
ict250 = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'ICT250')]
link = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'LINK2500')]
move5000 = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'MOVE/5000M')]
move5t = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'MOVE5000T')]
mp5 = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'MP5')]
mp5s = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'MP5S')]
p200 = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'P-200')]
pp920 = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'PIN PAD PPC920')]
pp930 = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'PPC930')]
s920 = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'S920')]
s920s = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'S920S')]
s920st = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'S920ST')]
c680 = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'C680')]

#EQUIPAMETNOS reversa
aposa_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'APOSA8')]
a910s_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'A910S')]
d195_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'D195')]
d195s_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'D195S')]
ict250_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa')  & (df['Esc01Descricao'] == 'ICT250')]
link_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa')  & (df['Esc01Descricao'] == 'LINK2500')]
move5000_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'MOVE/5000M')]
move5t_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'MOVE5000T')]
mp5_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa')  & (df['Esc01Descricao'] == 'MP5')]
mp5s_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa')  & (df['Esc01Descricao'] == 'MP5S')]
p200_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'P-200')]
pp920_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa')  & (df['Esc01Descricao'] == 'PIN PAD PPC920')]
pp930_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'PPC930')]
s920_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'S920')]
s920s_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa')  & (df['Esc01Descricao'] == 'S920S')]
s920st_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa')  & (df['Esc01Descricao'] == 'S920ST')]
c680_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa')  & (df['Esc01Descricao'] == 'C680')]

#CHIP GOOD
vivo = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'SIM CARD VIVO')]
vivo_trio =df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'SIM CARD VIVO TRIO')]
cinco = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'SIM CARD CINCO')]
cinco_trio =df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'SIM CARD CINCO TRIO')]
tim = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'SIM CARD TIM')]
tim_trio =df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'SIM CARD TIM TRIO')]
oi = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'SIM CARD OI')]
oi_trio =df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'SIM CARD OI TRIO')]
claro = df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'SIM CARD CLARO')]
claro_trio =df.loc[(df['SituacaoDescricao'] == 'Entrega confirmada no PA') & (df['SituacaoMovDescricao'] == 'Liberado') & (df['Esc01Descricao'] == 'SIM CARD CLARO TRIO')]

#CHIP BAD
vivo_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'SIM CARD VIVO')]
vivo_trio_bad =df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'SIM CARD VIVO TRIO')]
cinco_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'SIM CARD CINCO')]
cinco_trio_bad =df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'SIM CARD CINCO TRIO')]
tim_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'SIM CARD TIM')]
tim_trio_bad =df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'SIM CARD TIM TRIO')]
oi_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'SIM CARD OI')]
oi_trio_bad =df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'SIM CARD OI TRIO')]
claro_bad = df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'SIM CARD CLARO')]
claro_trio_bad =df.loc[(df['SituacaoDescricao'] == 'Entrada Logística Reversa') & (df['Esc01Descricao'] == 'SIM CARD CLARO TRIO')]


#RESETA INDEX DAS VARIAVEIS GOOD
oi_df = oi.reset_index(drop=True)
oi_trio_df = oi_trio.reset_index(drop=True)
claro_df = claro.reset_index(drop=True)
claro_trio_df = claro_trio.reset_index(drop=True)
tim_df = tim.reset_index(drop=True)
tim_trio_df = tim_trio.reset_index(drop=True)
cinco_df = cinco.reset_index(drop=True)
cinco_trio_df = cinco_trio.reset_index(drop=True)
vivo_df = vivo.reset_index(drop=True)
vivo_trio_df = vivo_trio.reset_index(drop=True)

#RESETA INDEX DAS VARIAVEIS BAD
oi_bad_df = oi_bad.reset_index(drop=True)
oi_trio_bad_df = oi_trio_bad.reset_index(drop=True)
claro_bad_df = claro_bad.reset_index(drop=True)
claro_trio_bad_df = claro_trio_bad.reset_index(drop=True)
tim_bad_df = tim_bad.reset_index(drop=True)
tim_trio_bad_df = tim_trio_bad.reset_index(drop=True)
cinco_bad_df = cinco_bad.reset_index(drop=True)
cinco_trio_bad_df = cinco_trio_bad.reset_index(drop=True)
vivo_bad_df = vivo_bad.reset_index(drop=True)
vivo_trio_bad_df = vivo_trio_bad.reset_index(drop=True)

#RESETA INDEX DAS VARIAVEIS EQUIPAMENTOS
aposa_df = aposa.reset_index(drop=True)
a910s_df = a910s.reset_index(drop=True)
d195_df = d195.reset_index(drop=True)
d195s_df = d195s.reset_index(drop=True)
ict250_df = ict250.reset_index(drop=True)
link_df = link.reset_index(drop=True)
move5000_df = move5000.reset_index(drop=True)
move5t_df = move5t.reset_index(drop=True)
mp5_df = mp5.reset_index(drop=True)
mp5s_df = mp5s.reset_index(drop=True)
p200_df = p200.reset_index(drop=True)
pp920_df = pp920.reset_index(drop=True)
pp930_df = pp930.reset_index(drop=True)
s920_df = s920.reset_index(drop=True)
s920s_df = s920s.reset_index(drop=True)
s920st_df = s920st.reset_index(drop=True)
c680_df = c680.reset_index(drop=True)

#RESETA INDEX DAS VARIAVEIS EQUIPAMENTOS bad
aposa_bad_df = aposa_bad.reset_index(drop=True)
a910s_bad_df = a910s_bad.reset_index(drop=True)
d195_bad_df = d195_bad.reset_index(drop=True)
d195s_bad_df = d195s_bad.reset_index(drop=True)
ict250_bad_df = ict250_bad.reset_index(drop=True)
link_bad_df = link_bad.reset_index(drop=True)
move5000_bad_df = move5000_bad.reset_index(drop=True)
move5t_bad_df = move5t_bad.reset_index(drop=True)
mp5_bad_df = mp5_bad.reset_index(drop=True)
mp5s_bad_df = mp5s_bad.reset_index(drop=True)
p200_bad_df = p200_bad.reset_index(drop=True)
pp920_bad_df = pp920_bad.reset_index(drop=True)
pp930_bad_df = pp930_bad.reset_index(drop=True)
s920_bad_df = s920_bad.reset_index(drop=True)
s920s_bad_df = s920s_bad.reset_index(drop=True)
s920st_bad_df = s920st_bad.reset_index(drop=True)
c680_bad_df = c680_bad.reset_index(drop=True)

#reseta rom exp pa
exp_pa_df = exp_pa.reset_index(drop=True)
coleta_df = coleta.reset_index(drop=True)

chip = cinco_df['Esc01Descricao'].value_counts(),cinco_trio_df['Esc01Descricao'].value_counts(),tim_df['Esc01Descricao'].value_counts(),tim_trio_df['Esc01Descricao'].value_counts(),vivo_df['Esc01Descricao'].value_counts(),vivo_trio_df['Esc01Descricao'].value_counts(),claro_df['Esc01Descricao'].value_counts(),claro_trio_df['Esc01Descricao'].value_counts(),oi_df['Esc01Descricao'].value_counts(),oi_trio_df['Esc01Descricao'].value_counts()
chip_bad = cinco_bad_df['Esc01Descricao'].value_counts(),cinco_trio_bad_df['Esc01Descricao'].value_counts(),tim_bad_df['Esc01Descricao'].value_counts(),tim_trio_bad_df['Esc01Descricao'].value_counts(),vivo_bad_df['Esc01Descricao'].value_counts(),vivo_trio_bad_df['Esc01Descricao'].value_counts(),claro_bad_df['Esc01Descricao'].value_counts(),claro_trio_bad_df['Esc01Descricao'].value_counts(),oi_bad_df['Esc01Descricao'].value_counts(),oi_trio_bad_df['Esc01Descricao'].value_counts()
estoque = aposa_df['Esc01Descricao'].value_counts(),a910s_df['Esc01Descricao'].value_counts(),ict250_df['Esc01Descricao'].value_counts(),d195_df['Esc01Descricao'].value_counts(),d195s_df['Esc01Descricao'].value_counts(),link_df['Esc01Descricao'].value_counts(),move5000_df['Esc01Descricao'].value_counts(),move5t_df['Esc01Descricao'].value_counts(),mp5_df['Esc01Descricao'].value_counts(),mp5s_df['Esc01Descricao'].value_counts(),p200_df['Esc01Descricao'].value_counts(),pp920_df['Esc01Descricao'].value_counts(),pp930_df['Esc01Descricao'].value_counts(),s920_df['Esc01Descricao'].value_counts(),s920s_df['Esc01Descricao'].value_counts(),s920st_df['Esc01Descricao'].value_counts(),c680_df['Esc01Descricao'].value_counts()
estoque_bad = aposa_bad_df['Esc01Descricao'].value_counts(),a910s_bad_df['Esc01Descricao'].value_counts(),ict250_bad_df['Esc01Descricao'].value_counts(),d195_bad_df['Esc01Descricao'].value_counts(),d195s_bad_df['Esc01Descricao'].value_counts(),link_bad_df['Esc01Descricao'].value_counts(),move5000_bad_df['Esc01Descricao'].value_counts(),move5t_bad_df['Esc01Descricao'].value_counts(),mp5_bad_df['Esc01Descricao'].value_counts(),mp5s_bad_df['Esc01Descricao'].value_counts(),p200_bad_df['Esc01Descricao'].value_counts(),pp920_bad_df['Esc01Descricao'].value_counts(),pp930_bad_df['Esc01Descricao'].value_counts(),s920_bad_df['Esc01Descricao'].value_counts(),s920s_bad_df['Esc01Descricao'].value_counts(),s920st_bad_df['Esc01Descricao'].value_counts(),c680_bad_df['Esc01Descricao'].value_counts()
todo_exp_rom_df = exp_pa_df['Romaneio'].value_counts()
coleta_df_rom_df = coleta_df['Romaneio'].value_counts()
volume_ag_col = len(coleta_df_rom_df)
volume_exp_col = len(todo_exp_rom_df)

root = tk.Tk()
root.title('Estoque Ingistal')
root.geometry('700x600')
root.resizable(False,False)
#responsive
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

color_1 = 'MediumSeagreen'
color_tit = 'MediumSeagreen'
color_2 = 'black'
color_3 = 'red'
white = "white"

var = StringVar(value=chip)
var_ativo = StringVar(value=estoque)

listbox1 = Listbox(root,width=15)
listbox1.grid(row=1, column=1,pady=40,padx=190)


listbox2 = Listbox(root, width=15,height=17)
listbox2.grid(row=2, column=1,pady=40)

listbox3 = Listbox(root, width=20)
listbox3.grid(row=1, column=2,padx=1)

listbox4 = Listbox(root, width=15,height=17)
listbox4.grid(row=2, column=2,padx=1)
listbox_chip_good = Listbox(root, width=8,height=1,bg=color_3, fg=white)
listbox_chip_good.place(relx=0.42,rely=0.35)
listbox_chip_bad = Listbox(root, width=8,height=1,bg=color_3, fg=white)
listbox_chip_bad.place(relx=0.85,rely=0.35)
listbox_equip_good = Listbox(root, width=8,height=1,bg=color_3, fg=white)
listbox_equip_good.place(relx=0.42,rely=0.95)
listbox_equip_bad = Listbox(root, width=8,height=1,bg=color_3, fg=white)
listbox_equip_bad.place(relx=0.85,rely=0.95)

listbox_ag_col_vol = Listbox(root, width=8,height=1,bg=color_3, fg=white)
listbox_ag_col_vol.place(relx=0.25,rely=0.09)
listbox_exp_col_vol = Listbox(root, width=8,height=1,bg=color_3, fg=white)
listbox_exp_col_vol.place(relx=0.25,rely=0.155)
listbox_ag_col = Listbox(root, width=8,height=1,bg=color_3, fg=white)
listbox_ag_col.place(relx=0.1,rely=0.09)
listbox_exp_rom = Listbox(root, width=8,height=1,bg=color_3, fg=white)
listbox_exp_rom.place(relx=0.1,rely=0.155)
listbox_exp = Listbox(root, width=8,height=1,bg=color_3, fg=white)
listbox_exp.place(relx=0.25,rely=0.125)
listbox_col = Listbox(root, width=8,height=1,bg=color_3, fg=white)
listbox_col.place(relx=0.25,rely=0.065)
listbox_pre = Listbox(root, width=8,height=1,bg=color_3, fg=white)
listbox_pre.place(relx=0.25,rely=0.185)
listbox_ngd = Listbox(root, width=8,height=1,bg=color_3, fg=white)
listbox_ngd.place(relx=0.25,rely=0.27)
listbox_gd = Listbox(root, width=8,height=1,bg=color_3, fg=white)
listbox_gd.place(relx=0.25,rely=0.3)
listbox_bd = Listbox(root, width=8,height=1,bg=color_3, fg=white)
listbox_bd.place(relx=0.25,rely=0.33)
listbox_doa = Listbox(root, width=8,height=1,bg=color_3, fg=white)
listbox_doa.place(relx=0.25,rely=0.36)
listbox_lib = Listbox(root, width=8,height=1,bg=color_3, fg=white)
listbox_lib.place(relx=0.25,rely=0.48)
listbox_bloq = Listbox(root, width=8,height=1,bg=color_3, fg=white)
listbox_bloq.place(relx=0.25,rely=0.51)
listbox_res = Listbox(root, width=8,height=1,bg=color_3, fg=white)
listbox_res.place(relx=0.25,rely=0.54)


sbar_V = tk.Scrollbar(root, orient = tk.VERTICAL, command=listbox1.yview)
listbox1.configure(yscrollcommand=sbar_V)
sbar_V.grid(row=1, column=4)
sbar_Y = tk.Scrollbar(root, orient = tk.VERTICAL, command=listbox2.yview)
listbox2.configure(yscrollcommand=sbar_Y)
sbar_Y.grid(row=2, column=4)

#titulo chip
txt1 = tk.Label(root, text='GOOD' ,bg="blue", fg="white")
txt1.place(relx=0.38,rely=0.028,relheight=.03,relwidth=.15)

#titulo equipamentos
txt2 = tk.Label(root, text='GOOD ' ,bg="blue", fg="white")
txt2.place(relx=0.38,rely=0.44,relheight=.03,relwidth=.15)

#ESTOQUE BAD 
txt3 = tk.Label(root, text='REVERSAR' ,bg="yellow", fg="black")
txt3.place(relx=0.81,rely=0.44,relheight=.03,relwidth=.15)
#CHIP BAD
txt4 = tk.Label(root, text='BAD' ,bg="yellow", fg="black")
txt4.place(relx=0.81,rely=0.028,relheight=.03,relwidth=.15)

#TITULO MODELO CHIP
txt5 = tk.Label(root, text='CHIP' ,bg=color_tit, fg=white)
txt5.place(relx=0.60,rely=0.028,relheight=.03,relwidth=.15)

#TITULO MODELO EQUIP
txt6= tk.Label(root, text='EQUIPAMENTO' ,bg=color_tit, fg=white)
txt6.place(relx=0.60,rely=0.44,relheight=.03,relwidth=.15)

#TITULO total contagem EQUIP
txt7= tk.Label(root, text='TOTAL' ,bg=color_3, fg=white)
txt7.place(relx=0.55,rely=0.95,relheight=.03,relwidth=.25)

#TITULO total contagem CHIP
txt8= tk.Label(root, text='TOTAL' ,bg=color_3, fg=white)
txt8.place(relx=0.54,rely=0.35,relheight=.03,relwidth=.25)

#titulo qtd
text_qtd1 = tk.Label(root, text='QTD', fg="black")
text_qtd1.place(relx=0.21,rely=0.035,relheight=.03,relwidth=.15)

#titulo qtd2
text_qtd2 = tk.Label(root, text='QTD', fg="black")
text_qtd2.place(relx=0.21,rely=0.24,relheight=.03,relwidth=.15)
#titulo total 1
text_tot1 = tk.Label(root, text='Total de Ativos', fg="black",bg=color_1)
text_tot1.place(relx=0.027,rely=0.22,relheight=.026,relwidth=.15)
#titulo total 2
text_tot = tk.Label(root, text='Total de Ativos', fg="black",bg=color_1)
text_tot.place(relx=0.027,rely=0.43,relheight=.026,relwidth=.15)
#titulo qtd3
text_qtd3 = tk.Label(root, text='QTD', fg="black")
text_qtd3.place(relx=0.21,rely=0.45,relheight=.03,relwidth=.15)

#titulo coleta
text_coleta = tk.Label(root, text='Aguardando Coleta: ', fg="black")
text_coleta.place(relx=-0.02,rely=0.065,relheight=.03,relwidth=.25)
#titulo romaneios coleta
text_rom = tk.Label(root, text='R: ', fg="black")
text_rom.place(relx=-0.04,rely=0.09,relheight=.03,relwidth=.15)
#titulo expedido p pa
text_exp_pa = tk.Label(root, text='Expedido para o PA: ', fg="black")
text_exp_pa.place(relx=-0.02,rely=0.125,relheight=.03,relwidth=.25)
#titulo romaneios expedido p pa
text_rom = tk.Label(root, text='R: ', fg="black")
text_rom.place(relx=-0.04,rely=0.155,relheight=.03,relwidth=.15)
#titulo presaida
text_pre= tk.Label(root, text='Pré-Saída: ', fg="black")
text_pre.place(relx=-.06,rely=0.185,relheight=.03,relwidth=.25)

#titulo liberado
text_lib= tk.Label(root, text='LIBERADO: ', fg="black")
text_lib.place(relx=-.06,rely=0.48,relheight=.03,relwidth=.25)

#titulo bloqueado
text_bloq= tk.Label(root, text='BLOQUEADO: ', fg="black")
text_bloq.place(relx=-.05,rely=0.51,relheight=.03,relwidth=.25)

#titulo reservado
text_res= tk.Label(root, text='RESERVADO: ', fg="black")
text_res.place(relx=-.055,rely=0.54,relheight=.03,relwidth=.25)

#titulo newgood
text_ngd= tk.Label(root, text='NEW GOOD: ', fg="black")
text_ngd.place(relx=-.05,rely=0.27,relheight=.03,relwidth=.25)
#titulo good
text_gd= tk.Label(root, text='GOOD: ', fg="black")
text_gd.place(relx=-.07,rely=0.3,relheight=.03,relwidth=.25)

#titulo BAD
text_bd= tk.Label(root, text='BAD: ', fg="black")
text_bd.place(relx=-.078,rely=0.33,relheight=.03,relwidth=.25)

#titulo DOA
text_doa= tk.Label(root, text='DOA: ', fg="black")
text_doa.place(relx=-.078,rely=0.36,relheight=.03,relwidth=.25)

#titulo chip
text_cinco = tk.Label(root, text='SIM CARD CINCO', fg="black")
text_cinco.place(relx=0.535,rely=0.065,relheight=.03,relwidth=.25)

text_cinco_trio = tk.Label(root, text='SIM CARD CINCO TRIO',bg=color_1, fg=white)
text_cinco_trio.place(relx=0.535,rely=0.09,relheight=.03,relwidth=.25)

text_tim = tk.Label(root, text='SIM CARD TIM', fg=color_2)
text_tim.place(relx=0.535,rely=0.118,relheight=.03,relwidth=.25)

text_tim_trio = tk.Label(root, text='SIM CARD TIM TRIO',bg=color_1, fg=white)
text_tim_trio.place(relx=0.535,rely=0.147,relheight=.028,relwidth=.25)

text_vivo = tk.Label(root, text='SIM CARD VIVO', fg=color_2)
text_vivo.place(relx=0.535,rely=0.17,relheight=.03,relwidth=.25)

text_vivo_trio = tk.Label(root, text='SIM CARD VIVO TRIO',bg=color_1, fg=white)
text_vivo_trio.place(relx=0.535,rely=0.2,relheight=.028,relwidth=.25)

text_claro = tk.Label(root, text='SIM CARD CLARO',fg=color_2)
text_claro.place(relx=0.535,rely=0.228,relheight=.03,relwidth=.25)

text_claro_trio = tk.Label(root, text='SIM CARD CLARO TRIO',bg=color_1, fg=white)
text_claro_trio.place(relx=0.535,rely=0.258,relheight=.028,relwidth=.25)

text_oi = tk.Label(root, text='SIM CARD OI', fg=color_2)
text_oi.place(relx=0.535,rely=0.285,relheight=.03,relwidth=.25)

text_oi_trio = tk.Label(root, text='SIM CARD OI TRIO',bg=color_1, fg=white)
text_oi_trio.place(relx=0.535,rely=0.31,relheight=.028,relwidth=.25)


#titulo chip
text_aposa8 = tk.Label(root, text='APOSA8', fg=color_2)
text_aposa8.place(relx=0.535,rely=0.475,relheight=.03,relwidth=.28)

text_a910s_trio = tk.Label(root, text='A910S',bg=color_1 ,fg=white)
text_a910s_trio.place(relx=0.535,rely=0.50,relheight=.03,relwidth=.28)

text_ict250 = tk.Label(root, text='ICT250', fg=color_2)
text_ict250.place(relx=0.535,rely=0.525,relheight=.03,relwidth=.28)


text_d195 = tk.Label(root, text='D195',bg=color_1 ,fg=white)
text_d195.place(relx=0.535,rely=0.55,relheight=.03,relwidth=.28)


text_d195s = tk.Label(root, text='D195S', fg=color_2)
text_d195s.place(relx=0.535,rely=0.575,relheight=.03,relwidth=.28)


text_link = tk.Label(root, text='LINK2500',bg=color_1 ,fg=white)
text_link.place(relx=0.535,rely=0.605,relheight=.03,relwidth=.28)

text_move5k = tk.Label(root, text='MOVE/5000', fg=color_2)
text_move5k.place(relx=0.535,rely=0.63,relheight=.03,relwidth=.28)

text_move5kt = tk.Label(root, text='MOVE/5000T',bg=color_1 ,fg=white)
text_move5kt.place(relx=0.535,rely=0.66,relheight=.03,relwidth=.28)

text_mp5 = tk.Label(root, text='MP5', fg=color_2)
text_mp5.place(relx=0.535,rely=0.685,relheight=.03,relwidth=.28)

text_mp5s = tk.Label(root, text='MP5S',bg=color_1,fg=white)
text_mp5s.place(relx=0.535,rely=0.71,relheight=.03,relwidth=.28)

text_p200 = tk.Label(root, text='P200', fg=color_2)
text_p200.place(relx=0.535,rely=0.738,relheight=.03,relwidth=.28)

text_pp920 = tk.Label(root, text='PPC920',bg=color_1 ,fg=white)
text_pp920.place(relx=0.535,rely=0.765,relheight=.03,relwidth=.28)
text_pp930 = tk.Label(root, text='PPC930', fg=color_2)
text_pp930.place(relx=0.535,rely=0.792,relheight=.03,relwidth=.28)
text_s920 = tk.Label(root, text='S920',bg=color_1 ,fg=white)
text_s920.place(relx=0.535,rely=0.822,relheight=.03,relwidth=.28)
text_s920s = tk.Label(root, text='S920S', fg=color_2)
text_s920s.place(relx=0.535,rely=0.848,relheight=.03,relwidth=.28)
text_s920st = tk.Label(root, text='S920ST',bg=color_1 ,fg=white)
text_s920st.place(relx=0.535,rely=0.875,relheight=.03,relwidth=.28)
text_c680 = tk.Label(root, text='C680', fg=color_2)
text_c680.place(relx=0.535,rely=0.905,relheight=.03,relwidth=.28)

#armazena os len da quantidade de equip para o insert
todo_equip = [len(aposa_df),len(a910s_df),len(ict250_df),len(d195_df),len(d195s_df),len(link_df),len(move5000_df),len(move5t_df),len(mp5_df),len(mp5s_df),len(p200_df),len(pp920_df),len(pp930_df),len(s920_df),len(s920s_df),len(s920st_df),len(c680_df)]
todo_chip_bad = [len(claro_bad_df),len(claro_trio_bad_df),len(vivo_bad_df),len(vivo_trio_bad_df),len(tim_bad_df),len(tim_trio_bad_df),len(cinco_bad_df),len(cinco_trio_bad_df),len(oi_bad_df),len(oi_trio_bad_df)]
todo_equip_bad = [len(aposa_bad_df),len(a910s_bad_df),len(ict250_bad_df),len(d195_bad_df),len(d195s_bad_df),len(link_bad_df),len(move5000_bad_df),len(move5t_bad_df),len(mp5_bad_df),len(mp5s_bad_df),len(p200_bad_df),len(pp920_bad_df),len(pp930_bad_df),len(s920_bad_df),len(s920s_bad_df),len(s920st_bad_df),len(c680_bad_df)]
todo_chip_good = [len(claro_df),len(claro_trio_df),len(vivo_df),len(vivo_trio_df),len(tim_df),len(tim_trio_df),len(cinco_df),len(cinco_trio_df),len(oi_df),len(oi_trio_df)]

def show_equip_good():
   soma_equip_good = 0
   for valor in todo_equip:
      soma_equip_good += valor
   return soma_equip_good

def show_equip_bad():
   soma_equip_bad = 0
   for valor in todo_equip_bad:
      soma_equip_bad += valor
   return soma_equip_bad

def show_chip_good():
   soma_chip_good = 0
   for valor in todo_chip_good:
      soma_chip_good += valor
   return soma_chip_good
def show_chip_bad():
   soma_chip_bad = []
   for valor in todo_chip_bad:
      soma_chip_bad.append(valor)
   return soma_chip_bad

listbox_equip_good.insert(END,show_equip_good())
listbox_equip_bad.insert(END,show_equip_bad())
listbox_chip_good.insert(END,show_chip_good())
listbox_chip_bad.insert(END,sum(todo_chip_bad))

listbox_col.insert(END,len(coleta))
listbox_exp.insert(END,len(exp_pa))
listbox_pre.insert(END,len(pre_saida))
listbox_ngd.insert(END,len(new_gd))
listbox_gd.insert(END,len(gd))
listbox_bd.insert(END,len(bd))
listbox_doa.insert(END,len(doa))
listbox_lib.insert(END,len(lib))
listbox_bloq.insert(END,len(bloq))
listbox_res.insert(END,len(res))
listbox_ag_col_vol.insert(END,volume_ag_col)
listbox_exp_col_vol.insert(END,volume_exp_col)
#insere valores na listbox de chip
for x,y in enumerate(chip): 
    listbox1.insert(x+1,int(y))
#insere valores na listbox de equip
for x in todo_equip:
   listbox2.insert(END,x)
for x in todo_equip_bad:
   listbox4.insert(END,x)
#insere valores na listbox de chip bad
for x in todo_chip_bad:
   listbox3.insert(END,x)
for i in range(len(todo_exp_rom_df)):
   listbox_exp_rom.insert(END,todo_exp_rom_df.index[i])
for i in range(len(coleta_df_rom_df)):
   listbox_ag_col.insert(END,coleta_df_rom_df.index[i])
root.mainloop()