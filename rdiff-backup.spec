
Summary:	Backup software
Name:		rdiff-backup
Version:	1.1.14
Release:	%mkrel 1
License:	GPL
Group:		Networking/Other
URL:		http://www.nongnu.org/rdiff-backup/
Source0:	http://download.savannah.nongnu.org/releases/rdiff-backup/%{name}-%{version}.tar.gz
# docs are already installed by %doc macro
Patch0:		rdiff-backup-1.1.11-dont-install-docs.patch
Requires:	python
BuildRequires:	librsync-devel >= 0.9.6
BuildRequires:	popt-devel
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-python
Epoch:		1

%description
rdiff-backup is a script, written in Python, that backs up one
directory to another and is intended to be run periodically
(nightly from cron for instance). The target directory ends up
a copy of the source directory, but extra reverse diffs are
stored in the target directory, so you can still recover files
lost some time ago. The idea is to combine the best features of
a mirror and an incremental backup. rdiff-backup can also operate
in a bandwidth efficient manner over a pipe, like rsync. Thus you
can use rdiff-backup and ssh to securely back a hard drive up to
a remote location, and only the differences from the previous
backup will be transmitted.

%prep
%setup -q
%patch0 -p1 -b .dont-install-docs

%build
python setup.py build

%install
rm -rf %{buildroot}
python \
	setup.py install \
	--optimize=2 \
	--root=%{buildroot}

%files
%defattr(644,root,root,755)
%doc CHANGELOG README FAQ.html examples.html COPYING
%attr(755,root,root) %{_bindir}/rdiff-backup
%attr(755,root,root) %{_bindir}/rdiff-backup-statistics
%dir %{py_platsitedir}/rdiff_backup
%{py_platsitedir}/rdiff_backup/*.py
%{py_platsitedir}/rdiff_backup/*.py[co]
%attr(755,root,root) %{py_platsitedir}/rdiff_backup/*.so
%{py_platsitedir}/rdiff_backup-*.egg-info
%{_mandir}/man1/rdiff-backup*

