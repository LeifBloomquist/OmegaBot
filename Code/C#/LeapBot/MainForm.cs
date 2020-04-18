using System;
using System.Drawing;
using System.Net.Sockets;
using System.Text;
using System.Windows.Forms;

namespace LeapMIDI
{
    public partial class MainForm : Form
    {
        LeapStuff leap = new LeapStuff();

        System.Drawing.Graphics graphicsObj = null;
        Pen redPen = new Pen(System.Drawing.Color.Red, 5);
        Pen yellowPen = new Pen(System.Drawing.Color.Yellow, 5);

        SimpleKalman kal_x = new SimpleKalman();
        SimpleKalman kal_y = new SimpleKalman();

        public MainForm()
        {
            InitializeComponent();

            graphicsObj = pictureBox1.CreateGraphics();

            System.Windows.Forms.Timer aTimer = new System.Windows.Forms.Timer();            
            aTimer.Tick += OnTimedEvent;
            aTimer.Interval = 50; // milliseconds
            aTimer.Enabled=true;
        }   

        // Specify what you want to happen when the Elapsed event is raised.
        private void OnTimedEvent(object source, EventArgs e)
        {
          leap.Update();
          LeapLabel.Text = leap.info;
          Animate();
          RobotControl();
        }

        private void RobotControl()
        {
            if (leap.hands != 1)
            {
                 SendLeftRight(0, 0);
                 return;
            }

            int MAX_SPEED = 50;

            float frontback = leap.posZ / -100f;
            float leftright = clamp(leap.posX / +100f, -1f, 1f);

            float ratio = (leftright + 1f) / 2f;  // 0 to 1, 0.5 in middle

            float left  = frontback * MAX_SPEED;
            float right = frontback * MAX_SPEED;

            left *= (1-ratio);
            right *= ratio;

            int ileft  = iclamp(left,  -MAX_SPEED, +MAX_SPEED);
            int iright = iclamp(right, -MAX_SPEED, +MAX_SPEED);

            SendLeftRight(ileft, iright);
        }

        private float clamp(float value, float min, float max)
        {
            if (value < min) value = min;
            if (value > max) value = max;
            return value;
        }

        private int iclamp(float value, float min, float max)
        {
            if (value < min) value = min;
            if (value > max) value = max;
            return (int)value;
        }

        private int clamp(int value, int min, int max)
        {
            if (value < min) value = min;
            if (value > max) value = max;
            return value;
        }

        private void SendUdp(int srcPort, string dstIp, int dstPort, byte[] data)
        {
            using (UdpClient c = new UdpClient(srcPort))
                c.Send(data, data.Length, dstIp, dstPort);
        }

        private void SendLeftRight(int left, int right)
        {
            String command = left.ToString() + "," + right.ToString();
            SendUdp(1000, "192.168.7.29", 2000, Encoding.ASCII.GetBytes(command));
            CommandLabel.Text = command;
        }

        private void Animate()
        {
            if (graphicsObj == null) return;

            graphicsObj.Clear(Color.Black);

            // Position

            float px = (pictureBox1.Width / 2f) + leap.posX;
            float py = (pictureBox1.Height) - leap.posY;
            float psize = 50 + (leap.posZ);
            try
            {
                graphicsObj.DrawEllipse(redPen, px, py, psize, psize);
            }
            catch { }

            // Motion

            float mx = (pictureBox1.Width / 2f) + leap.velX;
            float my = (pictureBox1.Height / 2f) - leap.velY;
            float msize = 5 + (leap.pinch * 10f);

            float kx = (float)kal_x.update(mx);
            float ky = (float)kal_y.update(my);

            graphicsObj.DrawEllipse(yellowPen, kx, ky, msize, msize);          
        }

        private void MainForm_Paint(object sender, PaintEventArgs e)
        {
          Animate();
        }

        private void MainForm_FormClosed(object sender, FormClosedEventArgs e)
        {
          Environment.Exit(0);
        }

        private void StopButton_Click(object sender, EventArgs e)
        {
            SendLeftRight(0, 0);
        }
    }
}
