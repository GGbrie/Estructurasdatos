using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ImprimirMatriz
{
    class ImprimirMatriz
    {
        private int[,] mat;

        public void Cargar() 
        {
            mat=new int[3,4];
            for(int f = 0; f < 3; f++) 
            {
                for(int c = 0; c < 4; c++) 
                {
                    Console.Write("---- Ingrese los Valores de la Matriz:");
                    string linea;
                    linea = Console.ReadLine();
                    mat[f,c]=int.Parse(linea);
                }
            }
        }

        public void PrimerFila() 
        {
    	    Console.WriteLine("---- La Primer Fila de la Matriz es ----");
            for(int c = 0; c < 4; c++) 
            {
                Console.WriteLine(mat[0,c]);
            }
        }
        public void UltimaFila() 
        {
    	    Console.WriteLine("---- La Ultima Fila es ----");
            for(int c = 0; c < 4; c++) 
            {
                Console.WriteLine(mat[2,c]);
            }
        }
        public void PrimerColumna() 
        {
    	    Console.WriteLine("---- La Primer Columna es ----");
            for(int f = 0; f < 3; f++) 
            {
                Console.WriteLine(mat[f,0]);
            }
        }

        static void Main(string[] args)
        {
            ImprimirMatriz m = new ImprimirMatriz();
            m.Cargar();
            m.PrimerFila();
            m.UltimaFila();
            m.PrimerColumna();
            Console.ReadKey();
        }
    }
}