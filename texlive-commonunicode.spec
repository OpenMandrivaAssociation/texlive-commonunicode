Name:		texlive-commonunicode
Version:	62901
Release:	2
Summary:	Convert common unicode symbols to LaTeX code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/commonunicode
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/commonunicode.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/commonunicode.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The aim of this LaTeX package is to provide a complete as
possible list of common Unicode symbols with their translations
to LaTeX code. This is useful in the development of templates
which are intended to work with modern TeX engines (LuaTeX,
XeTeX) as well as traditional ones (TeX, pdfTeX).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/commonunicode
%doc %{_texmfdistdir}/doc/latex/commonunicode

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
