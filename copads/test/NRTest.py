import sys
import os
import unittest


class testNR(unittest.TestCase):
#    def testadi(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testairy(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testamebsa(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testamoeba(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testanneal(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testanorm2(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testarcmak(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testarcode(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testarcsum(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testavevar(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbadluk(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbalanc(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbanbks(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbandec(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbanmul(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbcucof(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbcuint(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbeschb(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbessi(self): self.assertAlmostEqual(N.bessi(2.0, 10.0), 2281.5189)
#    def testbessi0(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbessi1(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbessik(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbessj(self): self.assertAlmostEqual(N.<something>( ), testdata)
    def testbessj0(self): self.assertAlmostEqual(N.bessj0(0.0), 1.0)
#    def testbessj1(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbessjy(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbessk(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbessk0(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbessk1(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbessy(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbessy0(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbessy1(self): self.assertAlmostEqual(N.<something>( ), testdata)
    def testbeta(self): self.assertAlmostEqual(N.beta(0.2, 1.0), 5.000000)
#    def testbetacf(self): self.assertAlmostEqual(N.<something>( ), testdata)
    def testbetai(self): self.assertAlmostEqual(N.betai(10.0, 5.0, 1.0), 1.000000)
#    def testbico(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbnldev(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbrent(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbroydn(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testbsstep(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testcaldat(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testcdf_binomial(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testcdf_poisson(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testcel(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testchder(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testchebev(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testchebpc(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testchebtf(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testchint(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testcholdc(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testcholsl(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testchsone(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testchstwo(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testcisi(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testcntab1(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testcntab2(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testconvlv(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testcorrel(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testcosft(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testcosft1(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testcosft2(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testcovsrt(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testcrank(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testcyclic(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testdaub4(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testdawson(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testdbrent(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testddpoly(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testdecchk(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testdes(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testdf1dim(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testdfpmin(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testdfridr(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testdftint(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testeclass(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testeclazz(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testei(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testeigsrt(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testel2(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testelle(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testellf(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testellpi(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testelmhes(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testerf(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testerfc(self): self.assertAlmostEqual(N.<something>( ), testdata)
    def testerfcc(self): self.assertAlmostEqual(N.erfcc(0.5), 0.479500092)
#    def testeulsum(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testevlmem(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testexpdev(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testexpint(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testf1dim(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testfactln(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testfactrl(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testfasper(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testfgauss(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testfit(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testfitexy(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testfixrts(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testfleg(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testflmoon(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testfour1(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testfourfs(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testfourn(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testfpoly(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testfred2(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testfredex(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testfredin(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testfrenel(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testfrprmn(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testftest(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testgamdev(self): self.assertAlmostEqual(N.<something>( ), testdata)
    def testgammln(self): self.assertAlmostEqual(N.gammln(0.5), 0.5723649)
    def testgammp(self): self.assertAlmostEqual(N.gammp(5.0, 5.0), 0.55950669)
    def testgammq(self): self.assertAlmostEqual(N.gammq(5.0, 5.0), 0.440493303)
#    def testgasdev(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testgaucof(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testgauher(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testgaujac(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testgaulag(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testgauleg(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testgaussj(self): self.assertAlmostEqual(N.<something>( ), testdata)
    def testgcf_0(self): self.assertAlmostEqual(N.gcf(5.0, 7.0)[0], 0.1729916)
    def testgcf_1(self): self.assertAlmostEqual(N.gcf(5.0, 7.0)[1], 3.17805383)
#    def testgolden(self): self.assertAlmostEqual(N.<something>( ), testdata)
    def testgser_1(self): self.assertAlmostEqual(N.gser(5.0, 5.0)[1], 3.17805383)
    def testgser_0(self): self.assertAlmostEqual(N.gser(5.0, 5.0)[0], 0.55950669)
#    def testhpsel(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testhpsort(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testhqr(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testhufapp(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testhufdec(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testhufenc(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testhufmak(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testhunt(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testhypdrv(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testhypgeo(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testhypser(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testicrc(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testicrc1(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testigray(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testindexx(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testirbit1(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testirbit2(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testjacobi(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testjulday(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testkendl1(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testkendl2(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testks2d1s(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testks2d2s(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testksone(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testkstwo(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testlaguer(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testlfit(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testlinbcg(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testlinmin(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testlnsrch(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testlocate(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testlop(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testlubksb(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testludcmp(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmachar(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmath(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmdian1(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmdian2(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmedfit(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmemcof(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmgfas(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmglin(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmidexp(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmidinf(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmidpnt(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmidsql(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmidsqu(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmiser(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmmid(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmnbrak(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmnewt(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmoment(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmp2dfr(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmpdiv(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmpinv(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmppi(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmprove(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmrqcof(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testmrqmin(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testnewt(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testodeint(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testorthog(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testpade(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testpccheb(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testpcshft(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testpearsn(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testperiod(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testpiksr2(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testpiksrt(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testplgndr(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testpoicoe(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testpoidev(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testpolcof(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testpoldiv(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testpolin2(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testpolint(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testpowell(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testpredic(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testprobks(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testpsdes(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testpwt(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testpwtest(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testpzextr(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testqcksrt(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testqgaus(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testqrdcmp(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testqromb(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testqromo(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testqroot(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testqrsolv(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testqrupdt(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testqsimp(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testqtrap(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testquad3d(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testquadvl(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testran0(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testran1(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testran2(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testran3(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testran4(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testrank(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testratint(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testratlsq(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testratval(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testrc(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testrd(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testrealft(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testrf(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testrj(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testrk4(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testrkdumb(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testrkqc(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testrkqs(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testrlft3(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testrofunc(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testrtbis(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testrtflsp(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testrtnewt(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testrtsafe(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testrtsec(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testrzextr(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsavgol(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testscrsho(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testselect(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testselip(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsfroid(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testshell(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testshoot(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testshootf(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsimplx(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsimpr(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsinft(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsmooft(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsncndn(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsobseq(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsolvde(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsor(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsort(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsort2(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsort3(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsparse(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testspctrm(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testspear(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsphbes(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsphfpt(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsphoot(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsplie2(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsplin2(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testspline(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsplint(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testspread(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsprsax(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsprsin(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsprspm(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsprstm(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsprstp(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsprstx(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def teststifbs(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def teststiff(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def teststoerm(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsvbksb(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsvdcmp(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsvdfit(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testsvdvar(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testtoeplz(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testtptest(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testtqli(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testtrapzd(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testtred2(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testtridag(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testttest(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testtutest(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testtwofft(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testvander(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testvegas(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testvoltra(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testwt1(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testwtn(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testwwghts(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testzbrac(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testzbrak(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testzbrent(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testzrhqr(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testzriddr(self): self.assertAlmostEqual(N.<something>( ), testdata)
#    def testzroots(self): self.assertAlmostEqual(N.<something>( ), testdata)

        
if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'src'))
    import NRPy as N
    unittest.main()