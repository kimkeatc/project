using NUnit.Framework;

namespace factorial.NUnitTest
{
    public class Tests
    {
        private factorial.Factorial _factorial_instance { get; set; } = null!;

        [SetUp]
        public void Setup()
        {
            _factorial_instance = new factorial.Factorial();
        }

        [Test]
        public void TestZero()
        {
            // Assign
            int number = 0;

            // Act
            int result = _factorial_instance.generate(number: number);

            // Assert
            Assert.AreEqual(1, result);
        }

        [Test]
        public void TestOne()
        {
            // Assign
            int number = 1;

            // Act
            int result = _factorial_instance.generate(number: number);

            // Assert
            Assert.AreEqual(1, result);
        }

        [Test]
        public void TestTwo()
        {
            // Assign
            int number = 2;

            // Act
            int result = _factorial_instance.generate(number: number);

            // Assert
            Assert.AreEqual(2, result);
        }

        [Test]
        public void TestThree()
        {
            // Assign
            int number = 3;

            // Act
            int result = _factorial_instance.generate(number: number);

            // Assert
            Assert.AreEqual(6, result);
        }

        [Test]
        public void TestFive()
        {
            // Assign
            int number = 5;

            // Act
            int result = _factorial_instance.generate(number: number);

            // Assert
            Assert.AreEqual(120, result);
        }
    }
}