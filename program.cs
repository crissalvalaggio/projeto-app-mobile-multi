using System;
using System.Windows.Forms;

namespace MeuAppDesktop
{
    public class Program : Form
    {
        private Button button;

        public Program()
        {
            // Configuração do formulário
            this.Text = "Meu App Desktop";
            this.Size = new System.Drawing.Size(300, 200);

            // Configuração do botão
            this.button = new Button();
            this.button.Text = "Clique Aqui!";
            this.button.Size = new System.Drawing.Size(100, 50);
            this.button.Location = new System.Drawing.Point(100, 50);
            this.button.Click += Button_Click;

            // Adiciona o botão ao formulário
            this.Controls.Add(this.button);
        }

        private void Button_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Olá, Mundo!");
        }

        public static void Main()
        {
            Application.Run(new Program());
        }
    }
}
