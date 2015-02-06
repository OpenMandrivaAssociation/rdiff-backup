
Summary:	Backup software
Name:		rdiff-backup
Version:	1.3.3
Release:	4
License:	GPLv2
Group:		Networking/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.nongnu.org/rdiff-backup/
Source0:	http://download.savannah.nongnu.org/releases/rdiff-backup/%{name}-%{version}.tar.gz
# from http://wiki.rdiff-backup.org/wiki/index.php/BashCompletion
Source1:	rdiff-backup.bash_completion
# docs are already installed by %doc macro
Patch0:		rdiff-backup-1.2.0-dont-install-docs.patch
Requires:	python
BuildRequires:	librsync-devel >= 0.9.6
BuildRequires:	popt-devel
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	python-rpm
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
# install bash_completion
mkdir -p -m 0755 %{buildroot}/%{_sysconfdir}/bash_completion.d
install -m 0644 %SOURCE1 %{buildroot}/%{_sysconfdir}/bash_completion.d/%name


%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc CHANGELOG README FAQ.html examples.html
%attr(755,root,root) %{_bindir}/rdiff-backup
%attr(755,root,root) %{_bindir}/rdiff-backup-statistics
%dir %{py_platsitedir}/rdiff_backup
%{py_platsitedir}/rdiff_backup/*.py
%attr(755,root,root) %{py_platsitedir}/rdiff_backup/*.so
%{py_platsitedir}/rdiff_backup-*.egg-info
%{_mandir}/man1/rdiff-backup*
%config(noreplace) %{_sysconfdir}/bash_completion.d/%name


%changelog
* Mon Nov 01 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1:1.3.3-3mdv2011.0
+ Revision: 591598
- fix file list

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1:1.3.3-2mdv2010.0
+ Revision: 442671
- rebuild

* Mon Mar 16 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.3.3-1mdv2009.1
+ Revision: 356038
- update to new version 1.3.3

* Tue Mar 03 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.3.2-1mdv2009.1
+ Revision: 348088
- update to new version 1.3.2

* Sun Feb 01 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.2.6-1mdv2009.1
+ Revision: 336155
- update to new version 1.2.6

* Mon Dec 29 2008 Frederik Himpe <fhimpe@mandriva.org> 1:1.2.3-1mdv2009.1
+ Revision: 321189
- update to new version 1.2.3

* Sun Dec 28 2008 Michael Scherer <misc@mandriva.org> 1:1.2.2-2mdv2009.1
+ Revision: 320254
- rebuild for new python

* Mon Oct 20 2008 Frederik Himpe <fhimpe@mandriva.org> 1:1.2.2-1mdv2009.1
+ Revision: 295835
- update to new version 1.2.2

  + Gaëtan Lehmann <glehmann@mandriva.org>
    - * add bash_completion
      * fix missing clean section and cleaning in install section

* Wed Aug 27 2008 Frederik Himpe <fhimpe@mandriva.org> 1:1.2.1-1mdv2009.0
+ Revision: 276623
- update to new version 1.2.1

* Thu Jul 31 2008 Frederik Himpe <fhimpe@mandriva.org> 1:1.2.0-1mdv2009.0
+ Revision: 256559
- New upstream version 1.2.0
- Update patch which prevents the setup script from intalling docs

* Wed Jun 18 2008 Frederik Himpe <fhimpe@mandriva.org> 1:1.1.16-1mdv2009.0
+ Revision: 225893
- update to new version 1.1.16

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Sun Feb 03 2008 Frederik Himpe <fhimpe@mandriva.org> 1:1.1.15-1mdv2008.1
+ Revision: 161722
- New upstream version
- Adapt to license policy

* Tue Aug 21 2007 Gaëtan Lehmann <glehmann@mandriva.org> 1:1.1.14-1mdv2008.0
+ Revision: 68253
- 1.1.14

* Tue Jul 24 2007 Gaëtan Lehmann <glehmann@mandriva.org> 1:1.1.12-1mdv2008.0
+ Revision: 55060
- 1.1.12

* Wed Jul 11 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:1.1.11-1mdv2008.0
+ Revision: 51407
- from Frederik Himpe:
  	o update to 1.1.11
  	o various cosmetics


* Fri Feb 23 2007 Gaëtan Lehmann <glehmann@mandriva.org> 1.1.9-1mdv2007.0
+ Revision: 124899
- 1.1.9

* Thu Nov 30 2006 Gaëtan Lehmann <glehmann@mandriva.org> 1:1.1.7-1mdv2007.1
+ Revision: 88996
- 1.1.7

* Wed Aug 09 2006 Gaëtan Lehmann <glehmann@mandriva.org> 1:1.0.4-1mdv2007.0
+ Revision: 54605
- rollback to stable release (1.0.4)
- Import rdiff-backup

* Fri Mar 10 2006 Jerome Soyer <saispo@mandriva.org> 1.1.5-1mdk
- New release 1.1.5

* Mon Jan 16 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.0.4-1mdk
- New release 1.0.4

* Wed Dec 14 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.0.3-1mdk
- 1.0.3
- update URL and source
- use mkrel

* Sat Apr 09 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.13.6-1mdk
- 0.13.6

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 0.13.4-2mdk
- Rebuild for new python

* Fri Oct 15 2004 Erwan Velu <erwan@mandrakesoft.com> 0.13.4-1mdk
- 0.13.4
- requires python

