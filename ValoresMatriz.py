using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ValoresMatriz
{
    class ValoresMatriz
    {
        private int[,] mat;

        public void Cargar() 
        {
            mat=new int[4,4];
            for(int f = 0; f < 4; f++) 
            {
                for(int c = 0; c<4; c++) 
                {
                    Console.Write("---- Ingrese los Valores de la Matriz: ");
                    string linea;
                    linea = Console.ReadLine();
                    mat[f, c] = int.Parse(linea);
                }
            }
        }

        public void ImprimirDiagonalPrincipal() 
        {
            for(int k = 0; k < 4; k++) 
            {
                Console.Write(mat[k,k]+" ");
            }
            Console.ReadKey();
        }

        static void Main(string[] args)
        {
            ValoresMatriz vm = new ValoresMatriz();
            vm.Cargar();
            vm.ImprimirDiagonalPrincipal();
        }
    }
}
