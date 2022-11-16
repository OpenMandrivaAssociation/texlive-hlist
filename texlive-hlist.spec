Name:		texlive-hlist
Version:	44983
Release:	1
Summary:	Horizontal and columned lists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hlist
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hlist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hlist.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This plain TeX and LaTeX package provides the "hlist"
environment in which \hitem starts a horizontal and columned
item. It depends upon the simplekv package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/hlist
%doc %{_texmfdistdir}/doc/generic/hlist

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
