# coding: utf-8

# This function computes the body mass index (BMI),
# given the height (in meter) and weight (in kg) of a person.


# This function returns the BMI category acording to this table:
# BMI:        <18.5         [18.5, 25[      [25, 30[      30 or greater 
# Category:   Underweight   Normal weight   Overweight    Obesity 

    


# This is the main function

def main():
    print("Índice de Massa Corporal")
    
    height = float(input("Altura (m)? "))
    if height < 0:
        print("ERRO: altura inválida!")
        exit(1)

    weight = float(input("Peso (kg)? "))
    if weight < 0:
        print("ERRO: peso inválido!")
        exit(1)

    def bodyMassIndex(height, weight):
        bmi = weight / (height**2)
        return bmi

    imc = bodyMassIndex(height, weight)
    print("BMI:", imc, "kg/m2")

    def bmiCategory(bmi):
        assert bmi>0
        if bmi<18.5:
            cat="Underweight"
        elif 18.5<=bmi<25:
            cat="Normal weight"
        elif 25<=bmi<30:
            cat="Overweight"
        elif 30<=bmi:
            cat="Obesity"
        return(cat)
    cat = bmiCategory(imc)
        
        
    print("BMI category:", cat)
        
# Program starts executing here
main()

