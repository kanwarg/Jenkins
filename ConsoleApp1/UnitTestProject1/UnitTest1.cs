using Microsoft.VisualStudio.TestTools.UnitTesting;

using ConsoleApp1;

namespace UnitTestProject1
{
    [TestClass]
    public class UnitTest1
    {

        [TestMethod]
        public void  CheckHello()
        {

            var result=ConsoleApp1.Program.SayHello();
            Assert.AreEqual("Hello", result);
        }


    }
}
