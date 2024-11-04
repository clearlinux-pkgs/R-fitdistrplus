#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v16
# autospec commit: b858a2a
#
Name     : R-fitdistrplus
Version  : 1.2.1
Release  : 59
URL      : https://cran.r-project.org/src/contrib/fitdistrplus_1.2-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fitdistrplus_1.2-1.tar.gz
Summary  : Help to Fit of a Parametric Distribution to Non-Censored or
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-rlang
BuildRequires : R-GeneralizedHyperbolic
BuildRequires : R-actuar
BuildRequires : R-rlang
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
to help the fit of a parametric distribution to non-censored or censored data. 
  Censored data may contain left censored, right censored and interval censored values, 
  with several lower and upper bounds. In addition to maximum likelihood estimation (MLE), 
  the package provides moment matching (MME), quantile matching (QME), maximum goodness-of-fit 
  estimation (MGE) and maximum spacing estimation (MSE) methods (available only for 
  non-censored data). Weighted versions of MLE, MME, QME and MSE are available. See e.g. 
  Casella & Berger (2002), Statistical inference, Pacific Grove, for a general introduction 
  to parametric estimation.

%prep
%setup -q -n fitdistrplus
pushd ..
cp -a fitdistrplus buildavx2
popd
pushd ..
cp -a fitdistrplus buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720801469

%install
export SOURCE_DATE_EPOCH=1720801469
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fitdistrplus/CITATION
/usr/lib64/R/library/fitdistrplus/DESCRIPTION
/usr/lib64/R/library/fitdistrplus/INDEX
/usr/lib64/R/library/fitdistrplus/Meta/Rd.rds
/usr/lib64/R/library/fitdistrplus/Meta/data.rds
/usr/lib64/R/library/fitdistrplus/Meta/features.rds
/usr/lib64/R/library/fitdistrplus/Meta/hsearch.rds
/usr/lib64/R/library/fitdistrplus/Meta/links.rds
/usr/lib64/R/library/fitdistrplus/Meta/nsInfo.rds
/usr/lib64/R/library/fitdistrplus/Meta/package.rds
/usr/lib64/R/library/fitdistrplus/Meta/vignette.rds
/usr/lib64/R/library/fitdistrplus/NAMESPACE
/usr/lib64/R/library/fitdistrplus/NEWS.md
/usr/lib64/R/library/fitdistrplus/R/fitdistrplus
/usr/lib64/R/library/fitdistrplus/R/fitdistrplus.rdb
/usr/lib64/R/library/fitdistrplus/R/fitdistrplus.rdx
/usr/lib64/R/library/fitdistrplus/data/danishmulti.rda
/usr/lib64/R/library/fitdistrplus/data/danishuni.rda
/usr/lib64/R/library/fitdistrplus/data/dataFAQlog1.rda
/usr/lib64/R/library/fitdistrplus/data/dataFAQscale1.rda
/usr/lib64/R/library/fitdistrplus/data/dataFAQscale2.rda
/usr/lib64/R/library/fitdistrplus/data/endosulfan.rda
/usr/lib64/R/library/fitdistrplus/data/fluazinam.rda
/usr/lib64/R/library/fitdistrplus/data/fremale.rda
/usr/lib64/R/library/fitdistrplus/data/groundbeef.rda
/usr/lib64/R/library/fitdistrplus/data/salinity.rda
/usr/lib64/R/library/fitdistrplus/data/smokedfish.rda
/usr/lib64/R/library/fitdistrplus/data/toxocara.rda
/usr/lib64/R/library/fitdistrplus/doc/FAQ.R
/usr/lib64/R/library/fitdistrplus/doc/FAQ.Rmd
/usr/lib64/R/library/fitdistrplus/doc/FAQ.html
/usr/lib64/R/library/fitdistrplus/doc/Optimalgo.R
/usr/lib64/R/library/fitdistrplus/doc/Optimalgo.Rmd
/usr/lib64/R/library/fitdistrplus/doc/Optimalgo.html
/usr/lib64/R/library/fitdistrplus/doc/fitdistrplus_vignette.R
/usr/lib64/R/library/fitdistrplus/doc/fitdistrplus_vignette.Rmd
/usr/lib64/R/library/fitdistrplus/doc/fitdistrplus_vignette.html
/usr/lib64/R/library/fitdistrplus/doc/index.html
/usr/lib64/R/library/fitdistrplus/doc/starting-values.R
/usr/lib64/R/library/fitdistrplus/doc/starting-values.Rmd
/usr/lib64/R/library/fitdistrplus/doc/starting-values.html
/usr/lib64/R/library/fitdistrplus/help/AnIndex
/usr/lib64/R/library/fitdistrplus/help/aliases.rds
/usr/lib64/R/library/fitdistrplus/help/fitdistrplus.rdb
/usr/lib64/R/library/fitdistrplus/help/fitdistrplus.rdx
/usr/lib64/R/library/fitdistrplus/help/paths.rds
/usr/lib64/R/library/fitdistrplus/html/00Index.html
/usr/lib64/R/library/fitdistrplus/html/R.css
/usr/lib64/R/library/fitdistrplus/tests/t-CIcdfplot.R
/usr/lib64/R/library/fitdistrplus/tests/t-Surv2fitdistcens.R
/usr/lib64/R/library/fitdistrplus/tests/t-bootdist.R
/usr/lib64/R/library/fitdistrplus/tests/t-bootdistcens.R
/usr/lib64/R/library/fitdistrplus/tests/t-cdfcomp.R
/usr/lib64/R/library/fitdistrplus/tests/t-cdfcompcens.R
/usr/lib64/R/library/fitdistrplus/tests/t-cvg-algo.R
/usr/lib64/R/library/fitdistrplus/tests/t-denscomp.R
/usr/lib64/R/library/fitdistrplus/tests/t-descdist.R
/usr/lib64/R/library/fitdistrplus/tests/t-detectbound.R
/usr/lib64/R/library/fitdistrplus/tests/t-fitbench.R
/usr/lib64/R/library/fitdistrplus/tests/t-fitdist-customoptim.R
/usr/lib64/R/library/fitdistrplus/tests/t-fitdist-hessianpb.R
/usr/lib64/R/library/fitdistrplus/tests/t-fitdist-test-arguments.R
/usr/lib64/R/library/fitdistrplus/tests/t-fitdist.R
/usr/lib64/R/library/fitdistrplus/tests/t-fitdistcens.R
/usr/lib64/R/library/fitdistrplus/tests/t-gen-max-spacing-estim.R
/usr/lib64/R/library/fitdistrplus/tests/t-getparam.R
/usr/lib64/R/library/fitdistrplus/tests/t-gofstat.R
/usr/lib64/R/library/fitdistrplus/tests/t-init-actuar.R
/usr/lib64/R/library/fitdistrplus/tests/t-llplot.R
/usr/lib64/R/library/fitdistrplus/tests/t-lnL-surf.R
/usr/lib64/R/library/fitdistrplus/tests/t-logLik-vcov-coef.R
/usr/lib64/R/library/fitdistrplus/tests/t-manageparam.R
/usr/lib64/R/library/fitdistrplus/tests/t-mgedist.R
/usr/lib64/R/library/fitdistrplus/tests/t-mledist-asymptotic-vcov.R
/usr/lib64/R/library/fitdistrplus/tests/t-mledist-cens.R
/usr/lib64/R/library/fitdistrplus/tests/t-mledist-nocens.R
/usr/lib64/R/library/fitdistrplus/tests/t-mledist-paramsupport.R
/usr/lib64/R/library/fitdistrplus/tests/t-mmedist-asymptotic-vcov.R
/usr/lib64/R/library/fitdistrplus/tests/t-mmedist.R
/usr/lib64/R/library/fitdistrplus/tests/t-msedist.R
/usr/lib64/R/library/fitdistrplus/tests/t-parallel.R
/usr/lib64/R/library/fitdistrplus/tests/t-plotdist.R
/usr/lib64/R/library/fitdistrplus/tests/t-plotdistcens.R
/usr/lib64/R/library/fitdistrplus/tests/t-ppcomp.R
/usr/lib64/R/library/fitdistrplus/tests/t-ppcompcens.R
/usr/lib64/R/library/fitdistrplus/tests/t-prefit.R
/usr/lib64/R/library/fitdistrplus/tests/t-qme-discrete.R
/usr/lib64/R/library/fitdistrplus/tests/t-qmedist.R
/usr/lib64/R/library/fitdistrplus/tests/t-qqcomp.R
/usr/lib64/R/library/fitdistrplus/tests/t-qqcompcens.R
/usr/lib64/R/library/fitdistrplus/tests/t-quantiledist.R
/usr/lib64/R/library/fitdistrplus/tests/t-startfixarg-overall.R
/usr/lib64/R/library/fitdistrplus/tests/t-starting-value-scale-rate.R
/usr/lib64/R/library/fitdistrplus/tests/t-startingvalues-fellerpareto-family.R
/usr/lib64/R/library/fitdistrplus/tests/t-startingvalues-invtrgamma-family.R
/usr/lib64/R/library/fitdistrplus/tests/t-startingvalues-othercont-family.R
/usr/lib64/R/library/fitdistrplus/tests/t-startingvalues-trgamma-family.R
/usr/lib64/R/library/fitdistrplus/tests/t-startingvalues-zeromod-family.R
/usr/lib64/R/library/fitdistrplus/tests/t-startingvalues-zerotrunc-family.R
/usr/lib64/R/library/fitdistrplus/tests/t-startingvalues.R
/usr/lib64/R/library/fitdistrplus/tests/t-util-mmedist-vcov.R
/usr/lib64/R/library/fitdistrplus/tests/t-util-npmle.R
/usr/lib64/R/library/fitdistrplus/tests/t-util-npsurv-mainfunction.R
/usr/lib64/R/library/fitdistrplus/tests/t-util-testdensity.R
/usr/lib64/R/library/fitdistrplus/tests/t-weird-ppcomp-cens.R
/usr/lib64/R/library/fitdistrplus/tests/t-weird-qqcomp-cens.R
