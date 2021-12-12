#include <iostream>
#include <complex>
#include <cmath>
#include <vector>
#include <iomanip> // to make the table
#include <chrono>  // btgeb el time bta3 el function
#include <algorithm>
#include <iterator>

using namespace std::chrono; //Time
using namespace std;

#ifndef M_PI

#define M_PI 3.14159265358979323846

#endif

typedef std::complex<double> Complex;

#ifdef __cplusplus

extern "C"
{

	void dft(complex<double> inp_sig[], complex<double> Output_Signal[], double Size);
	void fft(std::complex<double> input_signal[], int size);
}

#endif

void dft(complex<double> inp_sig[], complex<double> Output_Signal[], double Size)
{

	complex<double> int_sum;

	for (int k = 0; k < Size; k++)
	{
		int_sum = complex<double>(0, 0);
		// we will loop through each sample of our signal
		for (int n = 0; n < Size; n++)
		{
			double realPartCos = cos(((2 * M_PI) / Size) * k * n);
			double ImgPartSin = sin(((2 * M_PI) / Size) * k * n);
			complex<double> fourier_sig(realPartCos, -ImgPartSin);
			int_sum += inp_sig[n] * fourier_sig;
		}
		Output_Signal[k] = int_sum;
	}
}

void fft(std::complex<double> input_output_signal[], int size)
{
	const size_t N = size;
	if (N <= 1)
		return;

	int M = size / 2;

	std::complex<double> *even = new std::complex<double>[M];
	std::complex<double> *odd = new std::complex<double>[M];

	for (int i = 0; i < M; i++)
	{
		even[i] = input_output_signal[2 * i];
		odd[i] = input_output_signal[2 * i + 1];
	}

	// split
	fft(even, M);
	fft(odd, M);

	// combine
	for (size_t k = 0; k < N / 2; ++k)
	{
		std::complex<double> t = std::polar(1.0, -2 * M_PI * k / N) * odd[k];
		input_output_signal[k] = even[k] + t;
		input_output_signal[k + N / 2] = even[k] - t;
	}
}

int main()
{
}
