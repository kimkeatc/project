using NUnit.Framework;
using System;

namespace OddOrEven.NUnitTest
{
    public class Tests
    {

        private odd_or_even_v1.OddOrEven _instance_v1 { get; set; } = null!;
        private odd_or_even_v2.OddOrEven _instance_v2 { get; set; } = null!;

        [SetUp]
        public void Setup()
        {
            _instance_v1 = new odd_or_even_v1.OddOrEven();
            _instance_v2 = new odd_or_even_v2.OddOrEven();
        }

        [TestCase(1)]
        [TestCase(3)]
        [TestCase(5)]
        public void TestEvenIsFalse(int number)
        {
            // Act
            bool result_v1 = _instance_v1.is_even(number: number);
            bool result_v2 = _instance_v2.is_even(number: number);

            // Assert
            Assert.IsFalse(result_v1);
            Assert.IsFalse(result_v2);
        }

        [TestCase(2)]
        [TestCase(4)]
        [TestCase(6)]
        public void TestEvenIsTrue(int number)
        {
            // Act
            bool result_v1 = _instance_v1.is_even(number: number);
            bool result_v2 = _instance_v2.is_even(number: number);

            // Assert
            Assert.IsTrue(result_v1);
            Assert.IsTrue(result_v2);
        }

        [TestCase(2)]
        [TestCase(4)]
        [TestCase(6)]
        public void TestOddIsFalse(int number)
        {
            // Act
            bool result_v1 = _instance_v1.is_odd(number: number);
            bool result_v2 = _instance_v2.is_odd(number: number);

            // Assert
            Assert.IsFalse(result_v1);
            Assert.IsFalse(result_v2);
        }

        [TestCase(1)]
        [TestCase(3)]
        [TestCase(5)]
        public void TestOddIsTrue(int number)
        {
            // Act
            bool result_v1 = _instance_v1.is_odd(number: number);
            bool result_v2 = _instance_v2.is_odd(number: number);

            // Assert
            Assert.IsTrue(result_v1);
            Assert.IsTrue(result_v2);
        }
    }
}