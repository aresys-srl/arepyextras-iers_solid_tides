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

#ifndef SOLID_H_INCLUDED_
#define SOLID_H_INCLUDED_

#ifdef __cplusplus
extern "C"
{
#endif

#ifdef WIN32
    __declspec(dllexport)
#endif
        extern void solid(const double* i_glad, const double* i_glod, const int* i_yr, const int* i_mo, const int* i_dy,
                          double* o_tsecv, double* o_utv, double* o_vtv, double* o_wtv);

#ifdef __cplusplus
}
#endif

#endif
