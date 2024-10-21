<div class="Box-sc-g0xbh4-0 QkQOb js-snippet-clipboard-copy-unpositioned" data-hpc="true"><article class="markdown-body entry-content container-lg" itemprop="text"><div class="markdown-heading" dir="auto"><h1 tabindex="-1" class="heading-element" dir="auto" _msttexthash="217268558" _msthash="241">🔥DrugOOD🔥：AI 辅助药物发现的 OOD 数据集策展人和基准</h1><a id="user-content-firedrugoodfire--ood-dataset-curator-and-benchmark-for-ai-aided-drug-discovery" class="anchor" aria-label="永久链接： ：fire：DrugOOD：fire：： AI 辅助药物发现的 OOD 数据集策展人和基准" href="#firedrugoodfire--ood-dataset-curator-and-benchmark-for-ai-aided-drug-discovery" _mstaria-label="4985994" _msthash="242"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto" _msttexthash="175172504" _msthash="243">这是 DrugOOD 项目的正式实现，这是项目页面：<a href="https://drugood.github.io/" rel="nofollow" _istranslated="1">https://drugood.github.io/</a></p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto" _msttexthash="12344852" _msthash="244">环境安装</h2><a id="user-content-environment-installation" class="anchor" aria-label="永久链接：环境安装" href="#environment-installation" _mstaria-label="1038219" _msthash="245"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto" _msttexthash="123275815" _msthash="246">您可以使用提供的 drugood.yaml 文件安装 conda 环境：</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-k">!</span>git clone https://github.com/tencent-ailab/DrugOOD.git
<span class="pl-k">!</span>cd DrugOOD
<span class="pl-k">!</span>conda env create --name drugood --file=drugood.yaml
<span class="pl-k">!</span>conda activate drugood</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="!git clone https://github.com/tencent-ailab/DrugOOD.git
!cd DrugOOD
!conda env create --name drugood --file=drugood.yaml
!conda activate drugood" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font _mstmutation="1" _msttexthash="229276554" _msthash="247">然后，您可以转到演示，该演示提供了有关如何使用 DrugOOD 的快速练习。</font><code>demo/demo.ipynb</code></p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto" _msttexthash="5815212" _msthash="248">演示</h2><a id="user-content-demo" class="anchor" aria-label="永久链接： Demo" href="#demo" _mstaria-label="241150" _msthash="249"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font _mstmutation="1" _msttexthash="280558070" _msthash="250">有关使用 DrugOOD 进行数据集管理和 OOD 基准测试的快速实践，可以参考 。</font><code>demo/demo.ipynb</code></p>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto" _msttexthash="23000614" _msthash="251">数据集管理者</h2><a id="user-content-dataset-curator" class="anchor" aria-label="永久链接： 数据集策展人" href="#dataset-curator" _mstaria-label="593307" _msthash="252"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto" _msttexthash="711527752" _msthash="253">首先，您需要使用我们的代码生成所需的 DrugOOD 数据集。数据集策展人，目前专注于从 CHEMBL 生成数据集。它支持以下两项任务：</p>
<ul dir="auto">
<li _msttexthash="69821882" _msthash="254">基于配体的亲和预测 （LBAP）。</li>
<li _msttexthash="76656255" _msthash="255">基于结构的亲和力预测 （SBAP）。</li>
</ul>
<p dir="auto" _msttexthash="91654966" _msthash="256">对于 OOD 域注释，它支持以下 5 个选项。</p>
<ul dir="auto">
<li _msttexthash="6422819" _msthash="257">测定。</li>
<li _msttexthash="10328552" _msthash="258">脚手架。</li>
<li _msttexthash="5965791" _msthash="259">大小。</li>
<li _msttexthash="61964266" _msthash="260">蛋白。（仅适用于 SBAP 任务）</li>
<li _msttexthash="84346301" _msthash="261">蛋白质家族。（仅适用于 SBAP 任务）</li>
</ul>
<p dir="auto" _msttexthash="352942460" _msthash="262">对于噪声注释，它支持以下三个噪声级别。具有不同
噪声由具有不同严格级别的过滤器实现。</p>
<ul dir="auto">
<li _msttexthash="6415370" _msthash="263">核心。</li>
<li _msttexthash="6532708" _msthash="264">精制。</li>
<li _msttexthash="7300722" _msthash="265">常规。</li>
</ul>
<p dir="auto" _msttexthash="679002181" _msthash="266">同时，由于不同测量类型（例如 IC50、EC50、Ki、Potency）之间的转换不方便，因此需要在生成数据集时指定测量类型。</p>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto" _msttexthash="65641654" _msthash="267">如何运行和复制 96 个数据集？</h3><a id="user-content-how-to-run-and-reproduce-the-96-datasets" class="anchor" aria-label="永久链接： 如何运行和复制 96 个数据集？" href="#how-to-run-and-reproduce-the-96-datasets" _mstaria-label="1613976" _msthash="268"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font _mstmutation="1" _msttexthash="900163771" _msthash="269">首先，指定 CHEMBL 数据库的路径和目录，以便在配置中保存数据
file：用于 LBAP 任务或 SBAP 任务。<br _mstmutation="1" _istranslated="1">表示到
chembl29 sqllite 文件。指定用于保存生成数据的文件夹。</font><code>configs/_base_/curators/lbap_defaults.py</code><code>configs/_base_/curators/sbap_defaults.py</code><code>source_root="YOUR_PATH/chembl_29_sqlite/chembl_29.db"</code><code>target_root="data/"</code></p>
<p dir="auto"><font _mstmutation="1" _msttexthash="126033700" _msthash="270">请注意，您可以从 下载原始 sqllite 格式的 chembl29 数据库。</font><code>http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_29/chembl_29_sqlite.tar.gz</code></p>
<p dir="auto"><font _mstmutation="1" _msttexthash="842285444" _msthash="271">内置配置文件位于：<br _mstmutation="1" _istranslated="1"> 。这里我们提供了 96 个配置文件来<strong _mstmutation="1" _istranslated="1">复现</strong>我们论文中的 96 个数据集。同时
您还可以通过更改配置文件来自定义自己的数据集。</font><code>configs/curators/</code></p>
<p dir="auto"><font _mstmutation="1" _msttexthash="93328066" _msthash="272">运行 以生成数据集。以下是一些示例：</font><code>tools/curate.py</code></p>
<p dir="auto"><font _mstmutation="1" _msttexthash="125171085" _msthash="273">为 LBAP 任务生成数据集，其中 as domain 为 noise
level 作为 measurement type 和 task type。</font><code>assay</code><code>core</code><code>IC50</code><code>LBAP</code></p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>python tools/curate.py --cfg configs/curators/lbap_core_ic50_assay.py</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="python tools/curate.py --cfg configs/curators/lbap_core_ic50_assay.py" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font _mstmutation="1" _msttexthash="304050903" _msthash="274">为 SBAP 任务生成数据集，其中 as domain、 as noise level 和 as
测量类型，作为任务类型。</font><code>protein</code><code>refined</code><code>EC50</code><code>SBAP</code></p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>python tools/curate.py --cfg configs/curator/sbap_refined_ec50_protein.py</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="python tools/curate.py --cfg configs/curator/sbap_refined_ec50_protein.py" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto" _msttexthash="59368907" _msthash="275">对 SOTA OOD 算法进行基准测试</h2><a id="user-content-benchmarking-sota-ood-algorithms" class="anchor" aria-label="永久链接：对 SOTA OOD 算法进行基准测试" href="#benchmarking-sota-ood-algorithms" _mstaria-label="1286948" _msthash="276"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto" _msttexthash="86738613" _msthash="277">目前我们支持 6 种不同的基线算法：</p>
<ul dir="auto">
<li _msttexthash="22661626" _msthash="278">企业风险管理</li>
<li _msttexthash="54962336" _msthash="279">IRM （国际货币管理）</li>
<li _msttexthash="8648354" _msthash="280">GroupDro 公司</li>
<li _msttexthash="5795166" _msthash="281">珊瑚</li>
<li _msttexthash="4798989" _msthash="282">混合</li>
<li _msttexthash="4389099" _msthash="283">丹恩</li>
</ul>
<p dir="auto" _msttexthash="80474641" _msthash="284">同时，我们支持各种 GNN 骨干网：</p>
<ul dir="auto">
<li _msttexthash="6576076" _msthash="285">琴酒</li>
<li _msttexthash="7187050" _msthash="286">GCN 系列</li>
<li _msttexthash="6335914" _msthash="287">编织</li>
<li _msttexthash="7507539" _msthash="288">ShcNet 公司</li>
<li _msttexthash="23049" _msthash="289">GAT</li>
<li _msttexthash="6366438" _msthash="290">MGCN 公司</li>
<li _msttexthash="6489743" _msthash="291">NF 系列</li>
<li _msttexthash="96681" _msthash="292">ATi-FPGNN</li>
<li _msttexthash="206154" _msthash="293">GTransformer</li>
</ul>
<p dir="auto" _msttexthash="99062288" _msthash="294">以及用于蛋白质序列建模的不同主链：</p>
<ul dir="auto">
<li _msttexthash="4892381" _msthash="295">伯特</li>
<li _msttexthash="17348526" _msthash="296">蛋白质伯特</li>
</ul>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto" _msttexthash="22380215" _msthash="297">如何运行？</h3><a id="user-content-how-to-run" class="anchor" aria-label="永久链接：如何运行？" href="#how-to-run" _mstaria-label="391677" _msthash="298"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto" _msttexthash="70256732" _msthash="299">首先，运行以下命令进行安装。</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>python setup.py develop</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="python setup.py develop" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto" _msttexthash="57924087" _msthash="300">使用 ERM 算法运行 LBAP 任务：</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>python tools/train.py configs/algorithms/erm/lbap_core_ec50_assay_erm.py</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="python tools/train.py configs/algorithms/erm/lbap_core_ec50_assay_erm.py" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font _mstmutation="1" _msttexthash="424896537" _msthash="301">如果要在其他数据集上运行 ERM，请更改上述内容中的相应选项
config 文件。例如，指定输入数据。</font><code>ann_file = 'data/lbap_core_ec50_assay.json'</code></p>
<p dir="auto" _msttexthash="81558568" _msthash="302">同样，使用 ERM 算法运行 SBAP 任务：</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>python tools/train.py configs/algorithms/erm/sbap_core_ec50_assay_erm.py</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="python tools/train.py configs/algorithms/erm/sbap_core_ec50_assay_erm.py" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto" _msttexthash="5359406" _msthash="303">参考</h2><a id="user-content-reference" class="anchor" aria-label="永久链接：参考" href="#reference" _mstaria-label="396526" _msthash="304"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto" _msttexthash="203667789" _msthash="305">😄如果你觉得这个仓库有用，请考虑引用我们的论文：</p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>@ARTICLE{2022arXiv220109637J,
    author = {{Ji}, Yuanfeng and {Zhang}, Lu and {Wu}, Jiaxiang and {Wu}, Bingzhe and {Huang}, Long-Kai and {Xu}, Tingyang and {Rong}, Yu and {Li}, Lanqing and {Ren}, Jie and {Xue}, Ding and {Lai}, Houtim and {Xu}, Shaoyong and {Feng}, Jing and {Liu}, Wei and {Luo}, Ping and {Zhou}, Shuigeng and {Huang}, Junzhou and {Zhao}, Peilin and {Bian}, Yatao},
    title = "{DrugOOD: Out-of-Distribution (OOD) Dataset Curator and Benchmark for AI-aided Drug Discovery -- A Focus on Affinity Prediction Problems with Noise Annotations}",
    journal = {arXiv e-prints},
    keywords = {Computer Science - Machine Learning, Computer Science - Artificial Intelligence, Quantitative Biology - Quantitative Methods},
    year = 2022,
    month = jan,
    eid = {arXiv:2201.09637},
    pages = {arXiv:2201.09637},
    archivePrefix = {arXiv},
    eprint = {2201.09637},
    primaryClass = {cs.LG}
}
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="@ARTICLE{2022arXiv220109637J,
    author = {{Ji}, Yuanfeng and {Zhang}, Lu and {Wu}, Jiaxiang and {Wu}, Bingzhe and {Huang}, Long-Kai and {Xu}, Tingyang and {Rong}, Yu and {Li}, Lanqing and {Ren}, Jie and {Xue}, Ding and {Lai}, Houtim and {Xu}, Shaoyong and {Feng}, Jing and {Liu}, Wei and {Luo}, Ping and {Zhou}, Shuigeng and {Huang}, Junzhou and {Zhao}, Peilin and {Bian}, Yatao},
    title = &quot;{DrugOOD: Out-of-Distribution (OOD) Dataset Curator and Benchmark for AI-aided Drug Discovery -- A Focus on Affinity Prediction Problems with Noise Annotations}&quot;,
    journal = {arXiv e-prints},
    keywords = {Computer Science - Machine Learning, Computer Science - Artificial Intelligence, Quantitative Biology - Quantitative Methods},
    year = 2022,
    month = jan,
    eid = {arXiv:2201.09637},
    pages = {arXiv:2201.09637},
    archivePrefix = {arXiv},
    eprint = {2201.09637},
    primaryClass = {cs.LG}
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto" _msttexthash="12882805" _msthash="306">免責聲明</h2><a id="user-content-disclaimer" class="anchor" aria-label="永久链接： 免责声明" href="#disclaimer" _mstaria-label="434434" _msthash="307"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto" _msttexthash="55572543" _msthash="308">这不是官方支持的腾讯产品。</p>
</article></div>
