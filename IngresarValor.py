using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace sueldos_operadores
{
    class sueldos_operadores
    {
        private int[] sueldos;

        public void Cargar()
        {
            sueldos = new int[5];
            for (int f = 0; f < 5; f++)
            {
                Console.Write("Ingrese Valor del Sueldo:");
                String linea;
                linea = Console.ReadLine();
                sueldos[f] = int.Parse(linea);
            }
        }
        public void Imprimir() 
        {
            for(int f = 0; f < 5; f++) 
            {
                Console.WriteLine(sueldos[f]);
            }
            Console.ReadKey();
        }
        static void Main(string[] args)
        {
            sueldos_operadores pv = new sueldos_operadores();
            pv.Cargar();
            pv.Imprimir();
        }
    }
}