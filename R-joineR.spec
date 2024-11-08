#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-joineR
Version  : 1.2.8
Release  : 45
URL      : https://cran.r-project.org/src/contrib/joineR_1.2.8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/joineR_1.2.8.tar.gz
Summary  : Joint Modelling of Repeated Measurements and Time-to-Event Data
Group    : Development/Tools
License  : GPL-3.0
Requires: R-joineR-license = %{version}-%{release}
Requires: R-statmod
BuildRequires : R-statmod
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
effects joint models. Fits the joint models proposed by Henderson and colleagues

%package license
Summary: license components for the R-joineR package.
Group: Default

%description license
license components for the R-joineR package.


%prep
%setup -q -n joineR
cd %{_builddir}/joineR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1674498319

%install
export SOURCE_DATE_EPOCH=1674498319
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-joineR
cp %{_builddir}/joineR/LICENSE %{buildroot}/usr/share/package-licenses/R-joineR/12d81f50767d4e09aa7877da077ad9d1b915d75b || :
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/joineR/CITATION
/usr/lib64/R/library/joineR/DESCRIPTION
/usr/lib64/R/library/joineR/INDEX
/usr/lib64/R/library/joineR/LICENSE
/usr/lib64/R/library/joineR/Meta/Rd.rds
/usr/lib64/R/library/joineR/Meta/data.rds
/usr/lib64/R/library/joineR/Meta/features.rds
/usr/lib64/R/library/joineR/Meta/hsearch.rds
/usr/lib64/R/library/joineR/Meta/links.rds
/usr/lib64/R/library/joineR/Meta/nsInfo.rds
/usr/lib64/R/library/joineR/Meta/package.rds
/usr/lib64/R/library/joineR/Meta/vignette.rds
/usr/lib64/R/library/joineR/NAMESPACE
/usr/lib64/R/library/joineR/NEWS.md
/usr/lib64/R/library/joineR/R/joineR
/usr/lib64/R/library/joineR/R/joineR.rdb
/usr/lib64/R/library/joineR/R/joineR.rdx
/usr/lib64/R/library/joineR/data/Rdata.rdb
/usr/lib64/R/library/joineR/data/Rdata.rds
/usr/lib64/R/library/joineR/data/Rdata.rdx
/usr/lib64/R/library/joineR/doc/competing-risks.R
/usr/lib64/R/library/joineR/doc/competing-risks.Rmd
/usr/lib64/R/library/joineR/doc/competing-risks.html
/usr/lib64/R/library/joineR/doc/index.html
/usr/lib64/R/library/joineR/doc/joineR.R
/usr/lib64/R/library/joineR/doc/joineR.Rmd
/usr/lib64/R/library/joineR/doc/joineR.html
/usr/lib64/R/library/joineR/help/AnIndex
/usr/lib64/R/library/joineR/help/aliases.rds
/usr/lib64/R/library/joineR/help/figures/hex.png
/usr/lib64/R/library/joineR/help/joineR.rdb
/usr/lib64/R/library/joineR/help/joineR.rdx
/usr/lib64/R/library/joineR/help/paths.rds
/usr/lib64/R/library/joineR/html/00Index.html
/usr/lib64/R/library/joineR/html/R.css
/usr/lib64/R/library/joineR/tests/testthat.R
/usr/lib64/R/library/joineR/tests/testthat/Rplots.pdf
/usr/lib64/R/library/joineR/tests/testthat/test-ancillary.R
/usr/lib64/R/library/joineR/tests/testthat/test-comprisk.R
/usr/lib64/R/library/joineR/tests/testthat/test-misc.R
/usr/lib64/R/library/joineR/tests/testthat/test-models.R
/usr/lib64/R/library/joineR/tests/testthat/test-plot.R

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-joineR/12d81f50767d4e09aa7877da077ad9d1b915d75b
