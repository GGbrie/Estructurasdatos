using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace componentes
{
    class componentes
    {
        private float[] alturas;
        private float promedio;

        public void Cargar() 
        {
            alturas=new float[5];
            for (int f = 0; f < 5; f++)
            {
                Console.Write("Ingrese la Altura de una Persona:");
                string linea = Console.ReadLine();
                alturas[f] = float.Parse(linea);
            }
        }
    
        public void CalcularPromedio() 
        {
            float suma;
            suma=0;
            for(int f=0; f < 5; f++) 
            {
                suma=suma+alturas[f];
            }
            promedio=suma/5;
            Console.WriteLine("El Promedio Sera de:"+promedio);
        }

        public void MayoresMenores() 
        {
            int may,men;
            may=0;
            men=0;
            for(int f = 0; f < 5; f++) 
            {
                if (alturas[f] > promedio) 
                {
	                may++;
                }
                else
                {
                    if (alturas[f] < promedio) 
                    {
                        men++;
                    }
                }
            }
            Console.WriteLine("El Promedio Mayor fue de:"+may);
            Console.WriteLine("El Promedio Menor fue de :"+men);
            Console.ReadKey();
        }

        static void Main(string[] args)
        {
            componentes c2 = new componentes();
            c2.Cargar();
            c2.CalcularPromedio();
            c2.MayoresMenores();
        }
    }
}
