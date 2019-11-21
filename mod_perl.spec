#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xAB34BA0040E92ECE (stevehay@apache.org)
#
Name     : mod_perl
Version  : 2.0.11
Release  : 2
URL      : https://www.apache.org/dist/perl/mod_perl-2.0.11.tar.gz
Source0  : https://www.apache.org/dist/perl/mod_perl-2.0.11.tar.gz
Source1 : https://www.apache.org/dist/perl/mod_perl-2.0.11.tar.gz.asc
Summary  : An embedded Perl interpreter for the Apache Web server
Group    : Development/Tools
License  : Apache-1.1 Apache-2.0
Requires: mod_perl-bin = %{version}-%{release}
Requires: mod_perl-lib = %{version}-%{release}
Requires: mod_perl-license = %{version}-%{release}
Requires: mod_perl-perl = %{version}-%{release}
Requires: perl(Linux::Pid)
BuildRequires : apr-dev
BuildRequires : apr-util-dev
BuildRequires : buildreq-cpan
BuildRequires : expat-dev
BuildRequires : gdbm-dev
BuildRequires : httpd-dev
BuildRequires : httpd-extras
BuildRequires : util-linux-dev
Patch1: 0001-Fixup-installation-paths.patch

%description
Mod_perl incorporates a Perl interpreter into the Apache web server,
so that the Apache web server can directly execute Perl code.
Mod_perl links the Perl runtime library into the Apache web server and
provides an object-oriented Perl interface for Apache's C language
API.  The end result is a quicker CGI script turnaround process, since
no external Perl interpreter has to be started.

Install mod_perl if you're installing the Apache web server and you'd
like for it to directly incorporate a Perl interpreter.

%package bin
Summary: bin components for the mod_perl package.
Group: Binaries
Requires: mod_perl-license = %{version}-%{release}

%description bin
bin components for the mod_perl package.


%package dev
Summary: dev components for the mod_perl package.
Group: Development
Requires: mod_perl-lib = %{version}-%{release}
Requires: mod_perl-bin = %{version}-%{release}
Provides: mod_perl-devel = %{version}-%{release}
Requires: mod_perl = %{version}-%{release}

%description dev
dev components for the mod_perl package.


%package lib
Summary: lib components for the mod_perl package.
Group: Libraries
Requires: mod_perl-license = %{version}-%{release}

%description lib
lib components for the mod_perl package.


%package license
Summary: license components for the mod_perl package.
Group: Default

%description license
license components for the mod_perl package.


%package perl
Summary: perl components for the mod_perl package.
Group: Default
Requires: mod_perl = %{version}-%{release}

%description perl
perl components for the mod_perl package.


%prep
%setup -q -n mod_perl-2.0.11
cd %{_builddir}/mod_perl-2.0.11
%patch1 -p1

%build
## build_prepend content
export MP_APR_CONFIG=/usr/bin/apr-1-config
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mod_perl
cp %{_builddir}/mod_perl-2.0.11/Apache-Reload/LICENSE %{buildroot}/usr/share/package-licenses/mod_perl/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/mod_perl-2.0.11/Apache-SizeLimit/LICENSE %{buildroot}/usr/share/package-licenses/mod_perl/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/mod_perl-2.0.11/Apache-Test/LICENSE %{buildroot}/usr/share/package-licenses/mod_perl/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/mod_perl-2.0.11/LICENSE %{buildroot}/usr/share/package-licenses/mod_perl/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/mod_perl-2.0.11/NOTICE %{buildroot}/usr/share/package-licenses/mod_perl/97c92650e1f9ce20b0b9e82b6effb9653f0d5541
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mp2bug

%files dev
%defattr(-,root,root,-)
/usr/include/httpd/mod_perl.h
/usr/include/httpd/modperl_apache_compat.h
/usr/include/httpd/modperl_apache_includes.h
/usr/include/httpd/modperl_apr_compat.h
/usr/include/httpd/modperl_apr_includes.h
/usr/include/httpd/modperl_apr_perlio.h
/usr/include/httpd/modperl_bucket.h
/usr/include/httpd/modperl_callback.h
/usr/include/httpd/modperl_cgi.h
/usr/include/httpd/modperl_cmd.h
/usr/include/httpd/modperl_common_includes.h
/usr/include/httpd/modperl_common_log.h
/usr/include/httpd/modperl_common_types.h
/usr/include/httpd/modperl_common_util.h
/usr/include/httpd/modperl_config.h
/usr/include/httpd/modperl_const.h
/usr/include/httpd/modperl_constants.h
/usr/include/httpd/modperl_debug.h
/usr/include/httpd/modperl_directives.h
/usr/include/httpd/modperl_env.h
/usr/include/httpd/modperl_error.h
/usr/include/httpd/modperl_filter.h
/usr/include/httpd/modperl_flags.h
/usr/include/httpd/modperl_global.h
/usr/include/httpd/modperl_gtop.h
/usr/include/httpd/modperl_handler.h
/usr/include/httpd/modperl_hooks.h
/usr/include/httpd/modperl_interp.h
/usr/include/httpd/modperl_io.h
/usr/include/httpd/modperl_io_apache.h
/usr/include/httpd/modperl_largefiles.h
/usr/include/httpd/modperl_log.h
/usr/include/httpd/modperl_mgv.h
/usr/include/httpd/modperl_module.h
/usr/include/httpd/modperl_options.h
/usr/include/httpd/modperl_pcw.h
/usr/include/httpd/modperl_perl.h
/usr/include/httpd/modperl_perl_global.h
/usr/include/httpd/modperl_perl_includes.h
/usr/include/httpd/modperl_perl_pp.h
/usr/include/httpd/modperl_perl_unembed.h
/usr/include/httpd/modperl_svptr_table.h
/usr/include/httpd/modperl_sys.h
/usr/include/httpd/modperl_time.h
/usr/include/httpd/modperl_tipool.h
/usr/include/httpd/modperl_trace.h
/usr/include/httpd/modperl_types.h
/usr/include/httpd/modperl_util.h
/usr/include/httpd/modperl_xs_sv_convert.h
/usr/include/httpd/modperl_xs_typedefs.h
/usr/include/httpd/modperl_xs_util.h
/usr/share/man/man3/APR.3
/usr/share/man/man3/APR::Base64.3
/usr/share/man/man3/APR::Brigade.3
/usr/share/man/man3/APR::Bucket.3
/usr/share/man/man3/APR::BucketAlloc.3
/usr/share/man/man3/APR::BucketType.3
/usr/share/man/man3/APR::Const.3
/usr/share/man/man3/APR::Date.3
/usr/share/man/man3/APR::Error.3
/usr/share/man/man3/APR::Finfo.3
/usr/share/man/man3/APR::IpSubnet.3
/usr/share/man/man3/APR::OS.3
/usr/share/man/man3/APR::PerlIO.3
/usr/share/man/man3/APR::Pool.3
/usr/share/man/man3/APR::SockAddr.3
/usr/share/man/man3/APR::Socket.3
/usr/share/man/man3/APR::Status.3
/usr/share/man/man3/APR::String.3
/usr/share/man/man3/APR::Table.3
/usr/share/man/man3/APR::ThreadMutex.3
/usr/share/man/man3/APR::ThreadRWLock.3
/usr/share/man/man3/APR::URI.3
/usr/share/man/man3/APR::UUID.3
/usr/share/man/man3/APR::Util.3
/usr/share/man/man3/Apache2::Access.3
/usr/share/man/man3/Apache2::Build.3
/usr/share/man/man3/Apache2::CmdParms.3
/usr/share/man/man3/Apache2::Command.3
/usr/share/man/man3/Apache2::Connection.3
/usr/share/man/man3/Apache2::ConnectionUtil.3
/usr/share/man/man3/Apache2::Const.3
/usr/share/man/man3/Apache2::Directive.3
/usr/share/man/man3/Apache2::Filter.3
/usr/share/man/man3/Apache2::FilterRec.3
/usr/share/man/man3/Apache2::HookRun.3
/usr/share/man/man3/Apache2::Log.3
/usr/share/man/man3/Apache2::MPM.3
/usr/share/man/man3/Apache2::Module.3
/usr/share/man/man3/Apache2::PerlSections.3
/usr/share/man/man3/Apache2::Process.3
/usr/share/man/man3/Apache2::Reload.3
/usr/share/man/man3/Apache2::RequestIO.3
/usr/share/man/man3/Apache2::RequestRec.3
/usr/share/man/man3/Apache2::RequestUtil.3
/usr/share/man/man3/Apache2::Resource.3
/usr/share/man/man3/Apache2::Response.3
/usr/share/man/man3/Apache2::ServerRec.3
/usr/share/man/man3/Apache2::ServerUtil.3
/usr/share/man/man3/Apache2::SizeLimit.3
/usr/share/man/man3/Apache2::Status.3
/usr/share/man/man3/Apache2::SubProcess.3
/usr/share/man/man3/Apache2::SubRequest.3
/usr/share/man/man3/Apache2::URI.3
/usr/share/man/man3/Apache2::Util.3
/usr/share/man/man3/Apache2::compat.3
/usr/share/man/man3/Apache2::porting.3
/usr/share/man/man3/Apache::Reload.3
/usr/share/man/man3/Apache::SizeLimit.3
/usr/share/man/man3/Apache::SizeLimit::Core.3
/usr/share/man/man3/Apache::Test.3
/usr/share/man/man3/Apache::TestConfig.3
/usr/share/man/man3/Apache::TestHandler.3
/usr/share/man/man3/Apache::TestMB.3
/usr/share/man/man3/Apache::TestMM.3
/usr/share/man/man3/Apache::TestReport.3
/usr/share/man/man3/Apache::TestRequest.3
/usr/share/man/man3/Apache::TestRun.3
/usr/share/man/man3/Apache::TestRunPHP.3
/usr/share/man/man3/Apache::TestRunPerl.3
/usr/share/man/man3/Apache::TestServer.3
/usr/share/man/man3/Apache::TestSmoke.3
/usr/share/man/man3/Apache::TestTrace.3
/usr/share/man/man3/Apache::TestUtil.3
/usr/share/man/man3/Bundle::Apache2.3
/usr/share/man/man3/Bundle::ApacheTest.3
/usr/share/man/man3/ModPerl::BuildMM.3
/usr/share/man/man3/ModPerl::CScan.3
/usr/share/man/man3/ModPerl::Code.3
/usr/share/man/man3/ModPerl::Config.3
/usr/share/man/man3/ModPerl::Const.3
/usr/share/man/man3/ModPerl::Global.3
/usr/share/man/man3/ModPerl::MM.3
/usr/share/man/man3/ModPerl::MethodLookup.3
/usr/share/man/man3/ModPerl::PerlRun.3
/usr/share/man/man3/ModPerl::PerlRunPrefork.3
/usr/share/man/man3/ModPerl::Registry.3
/usr/share/man/man3/ModPerl::RegistryBB.3
/usr/share/man/man3/ModPerl::RegistryCooker.3
/usr/share/man/man3/ModPerl::RegistryLoader.3
/usr/share/man/man3/ModPerl::RegistryPrefork.3
/usr/share/man/man3/ModPerl::Util.3
/usr/share/man/man3/mod_perl2.3

%files lib
%defattr(-,root,root,-)
/usr/lib/httpd/modules/mod_perl.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mod_perl/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/mod_perl/97c92650e1f9ce20b0b9e82b6effb9653f0d5541

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/Base64.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/Brigade.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/Bucket.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/BucketAlloc.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/BucketType.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/Const.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/Date.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/Error.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/Finfo.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/IpSubnet.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/OS.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/PerlIO.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/Pool.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/SockAddr.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/Socket.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/Status.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/String.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/Table.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/ThreadMutex.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/ThreadRWLock.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/URI.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/UUID.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/Util.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/APR/XSLoader.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/Reload.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/SizeLimit.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/SizeLimit/Core.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/Test.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/Test5005compat.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestBuild.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestClient.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestCommon.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestCommonPost.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestConfig.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestConfigC.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestConfigPHP.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestConfigParrot.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestConfigParse.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestConfigPerl.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestHandler.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestHarness.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestHarnessPHP.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestMB.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestMM.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestPerlDB.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestReport.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestReportPerl.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestRequest.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestRun.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestRunPHP.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestRunParrot.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestRunPerl.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestSSLCA.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestServer.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestSmoke.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestSmokePerl.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestSort.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestTrace.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache/TestUtil.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/Access.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/Build.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/BuildConfig.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/CmdParms.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/Command.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/Connection.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/ConnectionUtil.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/Const.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/Directive.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/Filter.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/FilterRec.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/HookRun.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/Log.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/MPM.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/Module.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/ParseSource.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/PerlSections.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/PerlSections/Dump.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/Process.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/Provider.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/Reload.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/RequestIO.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/RequestRec.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/RequestUtil.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/Resource.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/Response.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/ServerRec.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/ServerUtil.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/SizeLimit.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/SourceTables.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/Status.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/SubProcess.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/SubRequest.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/URI.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/Util.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/XSLoader.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/compat.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Apache2/porting.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Bundle/Apache2.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Bundle/ApacheTest.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/BuildMM.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/BuildOptions.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/CScan.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/Code.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/Config.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/Const.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/FunctionMap.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/Global.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/InterpPool.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/Interpreter.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/MM.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/Manifest.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/MapUtil.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/MethodLookup.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/ParseSource.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/PerlRun.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/PerlRunPrefork.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/Registry.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/RegistryBB.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/RegistryCooker.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/RegistryLoader.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/RegistryPrefork.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/StructureMap.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/TestReport.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/TestRun.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/TiPool.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/TiPoolConfig.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/TypeMap.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/Util.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/ModPerl/WrapXS.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/APR.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/Base64/Base64.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/Brigade/Brigade.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/Bucket/Bucket.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/BucketAlloc/BucketAlloc.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/BucketType/BucketType.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/Const/Const.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/Date/Date.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/Error/Error.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/Finfo/Finfo.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/IpSubnet/IpSubnet.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/OS/OS.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/PerlIO/PerlIO.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/Pool/Pool.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/SockAddr/SockAddr.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/Socket/Socket.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/Status/Status.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/String/String.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/Table/Table.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/ThreadMutex/ThreadMutex.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/ThreadRWLock/ThreadRWLock.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/URI/URI.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/UUID/UUID.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/APR/Util/Util.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/Access/Access.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/Build/autosplit.ix
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/CmdParms/CmdParms.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/Command/Command.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/Connection/Connection.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/ConnectionUtil/ConnectionUtil.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/Const/Const.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/Directive/Directive.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/Filter/Filter.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/FilterRec/FilterRec.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/HookRun/HookRun.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/Log/Log.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/MPM/MPM.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/Module/Module.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/Process/Process.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/Provider/Provider.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/RequestIO/RequestIO.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/RequestRec/RequestRec.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/RequestUtil/RequestUtil.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/Response/Response.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/ServerRec/ServerRec.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/ServerUtil/ServerUtil.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/SubProcess/SubProcess.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/SubRequest/SubRequest.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/URI/URI.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/Util/Util.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Apache2/typemap
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/ModPerl/Const/Const.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/ModPerl/Global/Global.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/ModPerl/InterpPool/InterpPool.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/ModPerl/Interpreter/Interpreter.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/ModPerl/TiPool/TiPool.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/ModPerl/TiPoolConfig/TiPoolConfig.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/ModPerl/Util/Util.so
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/mod_perl2.pm
