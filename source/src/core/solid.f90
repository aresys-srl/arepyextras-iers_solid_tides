!
! Copyright (C) 2024 Aresys S.r.l. <info@aresys.it>
!
! This source code belongs to Aresys S.r.l., a duly registered company
! in MI, Italy whose principal place of business is Via Flumendosa 16,
! MI, Italy (Hereinafter: Licensor).
! You cannot modify, redistribute, transfer this source file or part
! of it nor create derivative work based on this.
! You can use this source file for the sole purposes defined in the
! contract that specifies your relationship with the Licensor and for
! the sole duration of the contract.
!

subroutine solid(i_glad, i_glod, i_yr, i_mo, i_dy, o_tsecv, o_utv, o_vtv, o_wtv) bind(C)
!DEC$ IF DEFINED(_WIN32)
!DEC$ ATTRIBUTES DLLEXPORT :: solid
!DEC$ END IF

    implicit none

    double precision :: i_glad, i_glod
    integer :: i_yr, i_mo, i_dy
    double precision, dimension(1441) :: o_tsecv, o_utv, o_vtv, o_wtv

    call solid_core(i_glad, i_glod, i_yr, i_mo, i_dy, o_tsecv, o_utv, o_vtv, o_wtv)
end subroutine solid
