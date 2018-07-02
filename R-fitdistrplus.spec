#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fitdistrplus
Version  : 1.0.9
Release  : 9
URL      : https://cran.r-project.org/src/contrib/fitdistrplus_1.0-9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fitdistrplus_1.0-9.tar.gz
Summary  : Help to Fit of a Parametric Distribution to Non-Censored or
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-GeneralizedHyperbolic
Requires: R-Hmisc
Requires: R-actuar
Requires: R-evaluate
Requires: R-highr
BuildRequires : R-GeneralizedHyperbolic
BuildRequires : R-Hmisc
BuildRequires : R-actuar
BuildRequires : R-evaluate
BuildRequires : R-highr
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n fitdistrplus

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521204596

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521204596
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fitdistrplus
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fitdistrplus
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fitdistrplus
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library fitdistrplus|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/fitdistrplus/NEWS
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
/usr/lib64/R/library/fitdistrplus/doc/index.html
/usr/lib64/R/library/fitdistrplus/doc/paper2JSS.R
/usr/lib64/R/library/fitdistrplus/doc/paper2JSS.Rnw
/usr/lib64/R/library/fitdistrplus/doc/paper2JSS.pdf
/usr/lib64/R/library/fitdistrplus/help/AnIndex
/usr/lib64/R/library/fitdistrplus/help/aliases.rds
/usr/lib64/R/library/fitdistrplus/help/fitdistrplus.rdb
/usr/lib64/R/library/fitdistrplus/help/fitdistrplus.rdx
/usr/lib64/R/library/fitdistrplus/help/paths.rds
/usr/lib64/R/library/fitdistrplus/html/00Index.html
/usr/lib64/R/library/fitdistrplus/html/R.css
