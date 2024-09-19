import flet as ft

def calc_suma(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1+num2
        lblResultado.value="Resultado: {resultado}"
    exept ValueError:
        lblResultado.value="Error,ingresa valores correctos"
        
def calc_resta(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1+num2
        lblResultado.value="Resultado: {resultado}"
    exept ValueError:
        lblResultado.value="Error,ingresa valores correctos"

def calc_multiplicacion(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1+num2
        lblResultado.value="Resultado: {resultado}"
    exept ValueError:
        lblResultado.value="Error,ingresa valores correctos"

def calc_division(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1+num2
        lblResultado.value="Resultado: {resultado}"
    exept ValueError:
        lblResultado.value="Error,ingresa valores correctos"

def main(page: ft.Page):
    page.title = "Calculadora"
    page.bgcolor= "Green"
    
    txtNum1=ft.Textfield(label"Ingresa el primer numero",color="yellow")

    txtNum1=ft.Textfield(label"Ingresa el segundo numero",color="yellow")
    lblResultado=ft.Text("Resultado: ",color"yellow")
    
    btnSuma=ft.ElevatedButton(text="+",on_click=on_calc_suma)
    btsResta=ft.ElevatedButton(text="-",on_click=on_calc_resta)
    btnMultiplicacion=ft.ElevatedButton(text="*",on_cal_multiplicacion)
    btnDivision=ft.ElevatedButton(text="/",on_click=on_calc_division)
    
    page.add(
        ft.Column(controls=[
            ft.Row(controls=[
                txtNum1,
                txtNum2
            ],aligment="center"),            
        ]),
        ft.Row(controls=[lblResultado],aligment="center"),
        ft.Row(controls=[
            btnSuma,
            btnResta,
            btnMultiplicacion,
            btnDivision
        ],aligment="center")
    )
ft.app(main)
