# set to nil when packaging a release, 
# or the long commit tag for the specific git branch
%define commit_tag 0b82c88bcf121daca22d24a62fa7590625d954e9
%define short_commit_tag 0b82c88bc

# when using a commit_tag (i.e. not nil) add a commit date
# decoration ~0.yyyyMMdd to Version number
%define commit_date 20251123

# their releases are not forthcoming, but the project is active
%define major_ver 2.6.1

# set to {nil} for a regular release
%define release_type weekly
%define dev_release .dev56+g

Name:           rdiff-backup
Version:        %{major_ver}%{?release_type:%{?dev_release}}%{?short_commit_tag}
Release:        2
Summary:        Reverse differential backup tool, over a network or locally
Group:          Utilities
License:        GPLv2
URL:            https://github.com/%name/%name/

# change the source URL depending on if the package is a release version or a git version
%if "%{commit_tag}" != "%{nil}"
Source0:        %url/archive/%{commit_tag}.tar.gz#/%name-%version.tar.gz
%else
Source0:        %url/archive/refs/tags/v%{version}.tar.gz#/%name-%version.tar.gz
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
%{_bindir}/%name
%{_bindir}/%name-delete
%{_bindir}/%name-statistics
%{python_sitearch}/rdiffbackup/
%{python_sitearch}/rdiff_backup*
%{_datadir}/bash-completion/completions/%name
%{_mandir}/man1/
%{_docdir}/%name/

