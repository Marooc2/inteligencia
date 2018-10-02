
package simulated2;

public class Simulated2 {
    public static double ProbabilidadAceptacion(int Energia, int NuevaEnergia, double Temperatura) {
        if (NuevaEnergia < Energia) {
            return 1.0;
        }
        return Math.exp((Energia - NuevaEnergia) / Temperatura);
    }
    public static void main(String[] args) {
        Ciudad ciudad1 = new Ciudad(5, 25);
        SeguimientoCiudades.addCity(ciudad1);
        Ciudad ciudad2 = new Ciudad(10,5);
        SeguimientoCiudades.addCity(ciudad2);
        Ciudad ciudad3 = new Ciudad(15, 35);
        SeguimientoCiudades.addCity(ciudad3);
        Ciudad ciudad4 = new Ciudad(20, 20);
        SeguimientoCiudades.addCity(ciudad4);
        Ciudad ciudad5 = new Ciudad(35, 40);
        SeguimientoCiudades.addCity(ciudad5);
        Ciudad ciudad6 = new Ciudad(40, 25);
        SeguimientoCiudades.addCity(ciudad6);
        Ciudad ciudad7 = new Ciudad(30, 10);
        SeguimientoCiudades.addCity(ciudad7);        
        
        double temp = 1000;

        double VelocidadEnfriamiento = 0.003;

        Tour SolucionActual = new Tour();
        SolucionActual.generateIndividual();
        
        Tour ElMejor = new Tour(SolucionActual.getTour());
        int Iteration=0,cont1=0,cont2=0;
        while (temp > 1) {
            Tour NuevaSolucion = new Tour(SolucionActual.getTour());

            int tourPos1 = (int) (NuevaSolucion.tourSize() * Math.random());
            int tourPos2 = (int) (NuevaSolucion.tourSize() * Math.random());

            Ciudad citySwap1 = NuevaSolucion.getCity(tourPos1);
            Ciudad citySwap2 = NuevaSolucion.getCity(tourPos2);
            
            NuevaSolucion.setCity(tourPos2, citySwap1);
            NuevaSolucion.setCity(tourPos1, citySwap2);
           
            int EnergiaActual = SolucionActual.getDistance();
            int EnergiaVecindad = NuevaSolucion.getDistance();


            double Prob = ProbabilidadAceptacion(EnergiaActual, EnergiaVecindad, temp);
            double Rand = Math.random();
            if (Prob > Rand) {
                SolucionActual = new Tour(NuevaSolucion.getTour());
                cont1++;
            }

            if (SolucionActual.getDistance() < ElMejor.getDistance()) {
                ElMejor = new Tour(SolucionActual.getTour());
                cont2++;
            }

            temp *= 1-VelocidadEnfriamiento;
            Iteration++;
        }
        System.out.println("Final solution distance: " + ElMejor.getDistance());
        System.out.println("Tour: " + ElMejor);
        System.out.println("Iteracion: " + Iteration);
        System.out.println("Reemplazos Solución actual: " + cont1);
        System.out.println("Reemplazos El mejor: " + cont2);
    }
}
