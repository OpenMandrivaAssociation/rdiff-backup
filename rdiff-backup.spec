# set to nil when packaging a release, 
# or the long commit tag for the specific git branch
%define commit_tag %{nil}

# when using a commit_tag (i.e. not nil) add a commit date
# decoration ~0.yyMMdd to Version number
%define commit_date %{nil}

# their releases are not forthcoming, but the project is active
%define major_ver 2.6.0

# set to {nil} for a regular release
%define unreleased 1

Name:           rdiff-backup
Version:        %{major_ver}%{?unreleased:+unreleased}%{?commit_date}
Release:        1
Summary:        Reverse differential backup tool, over a network or locally
Group:          Utilities
License:        GPLv2
URL:            https://github.com/%name/%name/archive/refs/tags

# change the source URL depending on if the package is a release version or a git version
%if "%{commit_tag}" != "%{nil}"
Source0:        https://github.com/<org_name>/<project_name>/archive/%{commit_tag}.tar.gz#/%{name}-%{version}.xz
%else
Source0:        %url/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

BuildSystem:    python

BuildRequires:  librsync-devel
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(python)
BuildRequires:  rdiff asciidoctor netcat

%description
rdiff-backup is a simple backup tool which can be used locally and remotely, 
on Linux and Windows, and even cross-platform between both. 
Users have reported using it successfully on FreeBSD and MacOS X.

%files
%license COPYING
%{_bindir}/
%{python_sitearch}/rdiffbackup/
%{python_sitearch}/rdiff_backup/
%{python_sitearch}/rdiff_backup-%{major_ver}.dist-info/
%{_datadir}/bash-completion/completions/%name
%{_mandir}/man1/
%{_docdir}/%name/

