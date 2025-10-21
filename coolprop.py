#Example 1
import CoolProp.CoolProp as CP

density = CP.PropsSI('D', 'T', 298.15, 'P', 101325, 'Water')
print(f"Density: {density:.2f} kg/m³")

#Example 2

state = CP.AbstractState('HEOS', 'Water')
state.update(CP.PT_INPUTS, 101325, 300)  # P=101325 Pa, T=300 K

h = state.hmass()    # Get enthalpy
s = state.smass()    # Get entropy  
rho = state.rhomass() # Get density

print(f"Enthalpy: {h/1000:.2f} kJ/kg")
print(f"Entropy: {s:.4f} J/kg·K") 
print(f"Density: {rho:.2f} kg/m³")

#Example 3
from CoolProp.Plots import PropertyPlot
plot = PropertyPlot('Air', 'Ts', unit_system='SI')
plot.calc_isolines()
plot.show()







