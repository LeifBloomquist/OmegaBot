using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeapMIDI
{
    public class FixedSizedQueue<T> : ConcurrentQueue<T>
    {
        private readonly object syncObject = new object();

        public int Size { get; private set; }

        public FixedSizedQueue(int size)
        {
            Size = size;
        }

        public new void Enqueue(T obj)
        {
            base.Enqueue(obj);
            lock (syncObject)
            {
                while (base.Count > Size)
                {
                    T outObj;
                    base.TryDequeue(out outObj);
                }
            }
        }
    }

    public class SimpleKalman
    {
    //    private double Q = 0.000001;
    //    private double R = 0.01;
        private double Q = 0.0001;
        private double R = 0.1;
        private double P = 1, X = 0, K;

        private void measurementUpdate()
        {
            K = (P + Q) / (P + Q + R);
            P = R * (P + Q) / (R + P + Q);
        }

        public double update(double measurement)
        {
            measurementUpdate();
            double result = X + (measurement - X) * K;
            X = result;
            return result;
        }
    }
}
