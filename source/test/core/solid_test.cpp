/*
 * Copyright (C) 2024 Aresys S.r.l. <info@aresys.it>
 *
 * This source code belongs to Aresys S.r.l., a duly registered company
 * in MI, Italy whose principal place of business is Via Flumendosa 16,
 * MI, Italy (Hereinafter: Licensor).
 * You cannot modify, redistribute, transfer this source file or part
 * of it nor create derivative work based on this.
 * You can use this source file for the sole purposes defined in the
 * contract that specifies your relationship with the Licensor and for
 * the sole duration of the contract.
 */

#include "core/solid.h"

#ifndef NDEBUG
#include <iostream>
#endif
#include <fstream>
#include <string>
#include <vector>

int main(int argc, char** argv)
{
    if (argc != 2)
    {
#ifndef NDEBUG
        std::cerr << "ERROR: wrong number of input arguments.\n"
                  << "Usage is as follows:\n"
                  << argv[0] << " <output_file>\n";
#endif

        return 1;
    }
    else
    {
        const std::string outputFile = argv[1];

        const double glad = 45.;
        const double glod = -100.;
        const int    yr   = 2000;
        const int    mo   = 1;
        const int    dy   = 1;

        std::vector<double> tsecv(1441);
        std::vector<double> utv(1441);
        std::vector<double> vtv(1441);
        std::vector<double> wtv(1441);

        solid(&glad, &glod, &yr, &mo, &dy, tsecv.data(), utv.data(), vtv.data(), wtv.data());

        std::ofstream outputFileStream(outputFile);
        outputFileStream.precision(5);
        for (std::size_t index = 0; index < 1441; ++index)
        {
            outputFileStream << tsecv[index] << ' ' << utv[index] << ' ' << vtv[index] << ' ' << wtv[index] << '\n';
        }

        return 0;
    }
}
