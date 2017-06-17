using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Leap;

namespace LeapMIDI
{
    class LeapStuff
    {
        private Controller controller = new Controller();

        public float posX { get; private set; }
        public float posY { get; private set; }
        public float posZ { get; private set; }

        public float velX { get; private set; }
        public float velY { get; private set; }
        public float velZ { get; private set; }

        public float pinch { get; private set; }

        public string info { get; private set; }

        public LeapStuff()
        {
            //controller.EnableGesture(Gesture.GestureType.;
            controller.SetPolicy(Controller.PolicyFlag.POLICY_BACKGROUND_FRAMES);
        }

        internal void Update()
        {        
            Frame frame = controller.Frame();

            info = "Connected: " + controller.IsConnected + "\n" +
                   "Frame ID: " + frame.Id + "\n" +
                   "Hands: " + frame.Hands.Count + "\n" +
                   "Fingers: " + frame.Fingers.Count + "\n\n";

            if (frame.Hands.Count == 1)
            {
                info += "Hand #1 Position X:" + frame.Hands[0].PalmPosition.x + "\n";
                info += "Hand #1 Position Y:" + frame.Hands[0].PalmPosition.y + "\n";
                info += "Hand #1 Position Z:" + frame.Hands[0].PalmPosition.z + "\n\n";

                info += "Hand #1 Velocity X:" + frame.Hands[0].PalmVelocity.x + "\n";
                info += "Hand #1 Velocity Y:" + frame.Hands[0].PalmVelocity.y + "\n";
                info += "Hand #1 Velocity Z:" + frame.Hands[0].PalmVelocity.z + "\n";

                info += "Hand #1 Pinch:" + frame.Hands[0].PinchStrength + "\n";

                posX = frame.Hands[0].PalmPosition.x;
                posY = frame.Hands[0].PalmPosition.y;
                posZ = frame.Hands[0].PalmPosition.z;

                velX = frame.Hands[0].PalmVelocity.x;
                velY = frame.Hands[0].PalmVelocity.y;
                velZ = frame.Hands[0].PalmVelocity.z;

                pinch = frame.Hands[0].PinchStrength;
            }
            else
            {
                velX = 0;
                velY = 0;
                velZ = 0;
                pinch = 0;
            }
        }
    }
}
